# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f140_general

import flatbuffers

class pvByte(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspvByte(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pvByte()
        x.Init(buf, n + offset)
        return x

    # pvByte
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pvByte
    def V(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def pvByteStart(builder): builder.StartObject(1)
def pvByteAddV(builder, v): builder.PrependInt8Slot(0, v, 0)
def pvByteEnd(builder): return builder.EndObject()