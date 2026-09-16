def hs_mux(sel, ls_hsi, hso):
    N = len(ls_hsi)
    ls_hsi_rdy, ls_hsi_vld = zip(*ls_hsi)
    ls_hsi_rdy, ls_hsi_vld = list(ls_hsi_rdy), list(ls_hsi_vld)
    hso_rdy, hso_vld = hso

    @always_comb
    def _hsmux():
        hso_vld.next = 0
        for i in range(N):
            ls_hsi_rdy[i].next = 0
            if i == sel:
                hso_vld.next = ls_hsi_vld[i]
                ls_hsi_rdy[i].next = hso_rdy
    return _hsmux