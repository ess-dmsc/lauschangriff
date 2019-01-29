# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f143_structure

import flatbuffers

class ArrayObj(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsArrayObj(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArrayObj()
        x.Init(buf, n + offset)
        return x

    # ArrayObj
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayObj
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Obj import Obj
            obj = Obj()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ArrayObj
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayObjStart(builder): builder.StartObject(1)
def ArrayObjAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayObjStartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArrayObjEnd(builder): return builder.EndObject()