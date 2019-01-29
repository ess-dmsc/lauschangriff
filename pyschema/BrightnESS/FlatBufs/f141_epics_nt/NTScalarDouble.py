# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class NTScalarDouble(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNTScalarDouble(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NTScalarDouble()
        x.Init(buf, n + offset)
        return x

    # NTScalarDouble
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NTScalarDouble
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def NTScalarDoubleStart(builder): builder.StartObject(1)
def NTScalarDoubleAddValue(builder, value): builder.PrependFloat64Slot(0, value, 0.0)
def NTScalarDoubleEnd(builder): return builder.EndObject()