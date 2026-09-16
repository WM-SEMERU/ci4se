def bitslice_select(offset, bv_di, bv_do):
    LEN_I = len(bv_di)
    LEN_O = len(bv_do)
    assert LEN_I >= LEN_O, 'bitslice_select: expects len(bv_di) >= len(bv_do), but len(bv_di)={}, len(bv_do)'.format(
        LEN_I, LEN_O)
    OFFSET_MAX = LEN_I - LEN_O + 1

    @always_comb
    def _slice():
        bv_do.next = 0
        for i in range(OFFSET_MAX):
            if i == offset:
                for b in range(LEN_O):
                    bv_do.next[b] = bv_di[i + b]
    return _slice