# Lauschangriff

This is a little tool which listens to Kafka topics and prints summaries of messages. It understands the 
following BrightnESS message formats:

- ev42, event data
- hs00, event histograms
- f142, epics-to-kafka data
- ns10, NICOS cache entries
- json, It prints the content of json command and status messages unchanged

 More message types can be easily added.

Lauschangriff supports listening continuously for messages, replaying messages for a time range given in IOS8601 time 
format and replaying from a manually specified offset. As of 12/2018 there is some confusion about timestamp formats on Kafka, 
thus replaying time rnages may not yet work properly. 

For usage information type:

    lauschangriff.py -h


