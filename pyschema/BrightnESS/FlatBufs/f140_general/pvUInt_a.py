# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f140_general

import flatbuffers

class pvUInt_a(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspvUInt_a(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pvUInt_a()
        x.Init(buf, n + offset)
        return x

    # pvUInt_a
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pvUInt_a
    def V(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # pvUInt_a
    def VAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # pvUInt_a
    def VLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pvUInt_aStart(builder): builder.StartObject(1)
def pvUInt_aAddV(builder, v): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(v), 0)
def pvUInt_aStartVVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def pvUInt_aEnd(builder): return builder.EndObject()