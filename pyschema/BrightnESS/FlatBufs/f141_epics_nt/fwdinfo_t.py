# automatically generated by the FlatBuffers compiler, do not modify

# namespace: f141_epics_nt

import flatbuffers

class fwdinfo_t(object):
    __slots__ = ['_tab']

    # fwdinfo_t
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # fwdinfo_t
    def Seq(self): return self._tab.Get(flatbuffers.number_types.Uint64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # fwdinfo_t
    def TsData(self): return self._tab.Get(flatbuffers.number_types.Uint64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # fwdinfo_t
    def TsFwd(self): return self._tab.Get(flatbuffers.number_types.Uint64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # fwdinfo_t
    def Fwdix(self): return self._tab.Get(flatbuffers.number_types.Uint8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # fwdinfo_t
    def Teamid(self): return self._tab.Get(flatbuffers.number_types.Uint64Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(32))

def Createfwdinfo_t(builder, seq, tsData, tsFwd, fwdix, teamid):
    builder.Prep(8, 40)
    builder.PrependUint64(teamid)
    builder.Pad(7)
    builder.PrependUint8(fwdix)
    builder.PrependUint64(tsFwd)
    builder.PrependUint64(tsData)
    builder.PrependUint64(seq)
    return builder.Offset()
