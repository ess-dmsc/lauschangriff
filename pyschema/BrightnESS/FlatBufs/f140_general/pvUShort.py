# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f140_general

import flatbuffers

class pvUShort(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspvUShort(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pvUShort()
        x.Init(buf, n + offset)
        return x

    # pvUShort
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pvUShort
    def V(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

def pvUShortStart(builder): builder.StartObject(1)
def pvUShortAddV(builder, v): builder.PrependUint16Slot(0, v, 0)
def pvUShortEnd(builder): return builder.EndObject()
