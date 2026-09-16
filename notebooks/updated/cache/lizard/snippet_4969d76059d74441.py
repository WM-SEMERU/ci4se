def prepare_w4():
    circ = qf.Circuit()
    circ += qf.X(1)
    circ += qf.ISWAP(1, 2) ** 0.5
    circ += qf.S(2)
    circ += qf.Z(2)
    circ += qf.ISWAP(2, 3) ** 0.5
    circ += qf.S(3)
    circ += qf.Z(3)
    circ += qf.ISWAP(0, 1) ** 0.5
    circ += qf.S(0)
    circ += qf.Z(0)
    ket = circ.run()
    return ket