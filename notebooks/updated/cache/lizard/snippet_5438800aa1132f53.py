def systemInformationType2():
    a = L2PseudoLength(l2pLength=22)
    b = TpPd(pd=6)
    c = MessageType(mesType=26)
    d = NeighbourCellsDescription()
    e = NccPermitted()
    f = RachControlParameters()
    packet = a / b / c / d / e / f
    return packet