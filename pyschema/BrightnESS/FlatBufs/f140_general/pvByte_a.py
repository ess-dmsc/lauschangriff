# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f140_general

import flatbuffers

class pvByte_a(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspvByte_a(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pvByte_a()
        x.Init(buf, n + offset)
        return x

    # pvByte_a
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pvByte_a
    def V(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # pvByte_a
    def VAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # pvByte_a
    def VLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pvByte_aStart(builder): builder.StartObject(1)
def pvByte_aAddV(builder, v): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(v), 0)
def pvByte_aStartVVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def pvByte_aEnd(builder): return builder.EndObject()
