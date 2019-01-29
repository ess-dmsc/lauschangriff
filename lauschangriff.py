#!/usr/bin/python
"""
  This is a little program which allows to listen to Kafa messages on a 
  specified number of topics. A summary of each message will be printed, 
  or, in the case of json command and status messages, the message itself 
  will be printed. This is meant as a streaming debugging tool.

  Mark Koennecke, December 2018    
"""

import argparse
from kafka import KafkaConsumer
from kafka import TopicPartition
import pyschema.EventMessage as ev42
import pyschema.LogData as ld
import pyschema.EventHistogram as hist
import pyschema.CacheEntry as ce10
from datetime import datetime
from dateutil import parser as timeparser
import time
import numpy
import pdb

# number types for Value conversions...
from pyschema.Double import Double
from pyschema.Float import Float
from pyschema.Int import Int
from pyschema.ArrayDouble import ArrayDouble
from pyschema.ArrayFloat import ArrayFloat
from pyschema.ArrayInt import ArrayInt
from pyschema.ArrayUInt  import ArrayUInt
from pyschema.ArrayULong  import ArrayULong
from pyschema.String  import String



"""
   Flatbuffer messages have an ID which live in bytes 4-8 of the message buffer.
   In printMessageSummary() there is a dictionary, msgProcessors, which holds 
   a flatbuffer message ID as a key and a function to process that message. Thus in 
   order to extend this to support more flatbuffer message types the follwoing needs 
   to be done:

   1. define a printXXXmessage(msg) function which knows how to decode the flatbuffer 
      message and prints a summary of it. You may need to import more classes for this. 
   2. Add the newly define function and the key tp msgProcessors in printMessageSummary()

   In order to make the output of lauschangriff processable by automatic tools, there is 
   a convention. The output should be key : value pairs separated by komma. If value 
   contains spaces, it should have quotes around it.

   There is another convention: ts is the raw timestamp which is usefule when ordering output with another 
   tool. tsh is a human readable timestamp for your fellow members of humanity

   Thats it. 
"""

def formatTSHuman(ts):
    dx = float(ts)/1000000000.
    dt = datetime.fromtimestamp(dx)
    return dt.isoformat()

def printEventMessage(msg):
    ev = ev42.EventMessage.GetRootAsEventMessage(bytearray(msg.value),0)
    print('type: ev42, nEvent: ' + str(ev.DetectorIdLength()) + ' ,topic: ' \
          + msg.topic + ' ,det: ' + ev.SourceName() + \
          ' ,ts:  ' +  str(ev.PulseTime())\
         + ',tsh: ' + formatTSHuman(ev.PulseTime()))

"""
  This is not complete....

  The vtype indexes into the order of entries into the Value union in f142_logdata.fbs
"""
def decodeLogValue(logmsg):
    vtype = logmsg.ValueType()
    val = logmsg.Value()
    if vtype == 5:
        x = Int()
        x.Init(val.Bytes,val.Pos)
        return str(x.Value())
    elif vtype == 9:
        x = Float()
        x.Init(val.Bytes,val.Pos)
        return str(x.Value())
    elif vtype == 10:
        x = Double()
        x.Init(val.Bytes,val.Pos)
        return str(x.Value())
    elif vtype == 15:
        x = ArrayInt()
        x.Init(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    elif vtype == 19:
        x = ArrayFloat()
        x.Initt(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    elif vtype == 20:
        x= ArrayDouble()
        x.Init(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    elif vtype == 21:
        x = String()
        x.Init(Val.Bytes,val.Pos);
        return x.Value()
    else:
        return 'ValueType ' + str(vtype) + ' not recognized yet'

def printLogMessage(msg):
    log = ld.LogData.GetRootAsLogData(bytearray(msg.value),0)
    val = decodeLogValue(log)
    print('type: f142, source: ' + log.SourceName() \
          + ',value: ' + val  \
          + ', ts: ' + str(log.Timestamp())\
          + ',tsh: ' + formatTSHuman(log.Timestamp()))

"""
  dtype indexes into the Array union in hs00_event_histogram.fbs
"""
def decodeHistValue(ls):
    dtype = ls.DataType()
    val = ls.Data()
    if dtype == 1:
        x = ArrayUInt()
        x.Init(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    elif dtype == 2:
        x = ArrayULong()
        x.Init(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    elif dtype == 3:
        x = ArrayDouble()
        x.Init(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    elif dtype == 4:
        x = ArrayFloat()
        x.Init(val.Bytes,val.Pos)
        xx = x.ValueAsNumpy()
        return str(numpy.sum(xx))
    else:
        return 'Type ' + str(dtype) + ' out of range' 

def printHistogram(msg):
    ls = hist.EventHistogram.GetRootAsEventHistogram(bytearray(msg.value),0)
    print('type: hs00, source: ' + ls.Source() \
          + ',counts: ' + decodeHistValue(ls) \
          + ',rank: ' + str(ls.CurrentShapeLength()) \
          + ', ts: ' + str(ls.Timestamp())\
          + ',tsh: ' + formatTSHuman(ls.Timestamp()) )


def printNSCache10(msg):
    entry = ce10.CacheEntry.GetRootAsCacheEntry(bytearray(msg.value),0)
    ts = entry.Time()
    dt = datetime.fromtimestamp(ts);
    print('type: ns10, key: ' + entry.Key() \
          + ',value: ' + entry.Value() \
          + ', ts: ' + str(entry.Time()) \
          + ',tsh: ' + dt.isoformat() )

def printNSCache11(msg):
    entry = ce10.GetRootAsCacheEntry(bytearray(msg.value),0)
    ts = entry.Time()
    dt = datetime.fromtimestamp(ts);
# TODO: As above, try to get at the Value if it is not an array
    print('type: ns11, key: ' + entry.Key() \
          + ', ts: ' + entry.Time()\
          + ',tsh: ' + dt.datetime.isoformat() )
    


def printMessageSummary(msg):
    msgProcessors = {}
    msgProcessors['ev42'] = printEventMessage   
    msgProcessors['f142'] = printLogMessage
    msgProcessors['hs00'] = printHistogram
#    msgProcessors['ns11'] = printNSCache11 not in use, 12/2018
    msgProcessors['ns10'] = printNSCache10
 
    msgID = msg.value[4:8]
    if msgProcessors.has_key(msgID):
       msgProcessors[msgID](msg)
    elif msg.value[0] == '{':
       print('topic: ' + msg.topic +' json: '+  msg.value)
    else:
       print('Received unknown message of possible type ' + msgID 
             + ' from topic ' +msg.topic)

def configureOffset(consumer,args):
    partlist = []
    for topic in args.topics:
        part = TopicPartition(topic,0)
        partlist.append(part)

    consumer.assign(partlist)
    for part in partlist:
        consumer.seek(part,int(args.offset))
    
    
def configureRange(consumer,args):
    partlist = []
    for topic in args.topics:
        part = TopicPartition(topic,0)
        partlist.append(part)
    dt = timeparser.parse(args.start)
    dtend = timeparser.parse(args.end)
    timestamps= {}
    endstamps = {}
#    multiplier = 1000000000 #This is for nanoseconds
    multiplier = 1000 # For milliseconds
    for part in partlist:
        timestamps[part] = time.mktime(dt.timetuple())*multiplier
        endstamps[part] = time.mktime(dtend.timetuple())*multiplier
    start_offsets = consumer.offsets_for_times(timestamps)
    end_offsets = consumer.offsets_for_times(endstamps)
    endoffset = None
    for part in partlist:
        if start_offsets[part] == None:
            print('No data found in the time range for topic ' + part.topic)
            return endoffset, False
        if end_offsets[part] != None:
            curoffset = end_offsets[part].offset
            if endoffset == None:
                endoffset = curoffset
            elif curoffset > endoffset:
                endoffset = curoffset

        """
        print(timestamps[part])
        print(str(dt.timetuple()) + ' timestamp ' + str(time.mktime(dt.timetuple())))
        print(str(dtend.timetuple()) + ' timestamp ' + str(time.mktime(dtend.timetuple())))
        print(start_offsets)
        print(end_offsets)
        """

    consumer.assign(partlist)
    for part in partlist:
        consumer.seek(part,start_offsets[part].offset)

    return endoffset, True
        

def lausch(args):
    consumer = KafkaConsumer(bootstrap_servers=args.broker)
    endoffset = None
    if args.start != None and args.end != None:
        endoffset, success = configureRange(consumer,args)
        if not success:
            return
    elif args.offset != None:
        configureOffset(consumer,args)
    else:
        consumer.subscribe(args.topics)

    for msg in consumer:
        printMessageSummary(msg)
        if endoffset != None:
            if msg.offset > endoffset:
                return

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Listen to BrightnESS Kafka messages')
    parser.add_argument('-s','--start',help="A start time in ISO8660 format from when to replay messages")
    parser.add_argument('-e','--end',help="A end time in ISO8660 format at which to stop replaying messages")
    parser.add_argument('-o','--offset',help="Directly specify an offset")
    parser.add_argument('broker',help='The Kafka Broker to connect to')
    parser.add_argument('topics',nargs='+',help='The list of topics to listen to')
    args = parser.parse_args()

    try:
        lausch(args)
    except KeyboardInterrupt:
        print("Finishing listening")

