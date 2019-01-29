# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class NTScalarArrayUByte(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNTScalarArrayUByte(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NTScalarArrayUByte()
        x.Init(buf, n + offset)
        return x

    # NTScalarArrayUByte
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NTScalarArrayUByte
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # NTScalarArrayUByte
    def ValueAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # NTScalarArrayUByte
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def NTScalarArrayUByteStart(builder): builder.StartObject(1)
def NTScalarArrayUByteAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def NTScalarArrayUByteStartValueVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def NTScalarArrayUByteEnd(builder): return builder.EndObject()
