# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class NTScalarShort(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNTScalarShort(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NTScalarShort()
        x.Init(buf, n + offset)
        return x

    # NTScalarShort
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NTScalarShort
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def NTScalarShortStart(builder): builder.StartObject(1)
def NTScalarShortAddValue(builder, value): builder.PrependInt16Slot(0, value, 0)
def NTScalarShortEnd(builder): return builder.EndObject()
