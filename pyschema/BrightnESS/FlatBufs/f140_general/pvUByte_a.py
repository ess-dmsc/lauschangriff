# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f140_general

import flatbuffers

class pvUByte_a(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspvUByte_a(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pvUByte_a()
        x.Init(buf, n + offset)
        return x

    # pvUByte_a
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pvUByte_a
    def V(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # pvUByte_a
    def VAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # pvUByte_a
    def VLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pvUByte_aStart(builder): builder.StartObject(1)
def pvUByte_aAddV(builder, v): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(v), 0)
def pvUByte_aStartVVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def pvUByte_aEnd(builder): return builder.EndObject()