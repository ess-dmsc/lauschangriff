# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class GEMTrack(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGEMTrack(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GEMTrack()
        x.Init(buf, n + offset)
        return x

    # GEMTrack
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GEMTrack
    def TimeOffset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # GEMTrack
    def Xtrack(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .pos import pos
            obj = pos()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GEMTrack
    def XtrackLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GEMTrack
    def Ytrack(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .pos import pos
            obj = pos()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GEMTrack
    def YtrackLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GEMTrack
    def Xpos(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

    # GEMTrack
    def Ypos(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0.0

def GEMTrackStart(builder): builder.StartObject(5)
def GEMTrackAddTimeOffset(builder, timeOffset): builder.PrependUint64Slot(0, timeOffset, 0)
def GEMTrackAddXtrack(builder, xtrack): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(xtrack), 0)
def GEMTrackStartXtrackVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GEMTrackAddYtrack(builder, ytrack): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(ytrack), 0)
def GEMTrackStartYtrackVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GEMTrackAddXpos(builder, xpos): builder.PrependFloat64Slot(3, xpos, 0.0)
def GEMTrackAddYpos(builder, ypos): builder.PrependFloat64Slot(4, ypos, 0.0)
def GEMTrackEnd(builder): return builder.EndObject()
