# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f143_structure

import flatbuffers

class Long(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLong(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Long()
        x.Init(buf, n + offset)
        return x

    # Long
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Long
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def LongStart(builder): builder.StartObject(1)
def LongAddValue(builder, value): builder.PrependInt64Slot(0, value, 0)
def LongEnd(builder): return builder.EndObject()
