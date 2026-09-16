def ram_sdp_rf(clk, we, addrw, addrr, di, do):
    memL = [Signal(intbv(0)[len(di):]) for _ in range(2 ** len(addrr))]

    @always(clk.posedge)
    def write():
        if we:
            memL[int(addrw)].next = di
        do.next = memL[int(addrr)]
    return write