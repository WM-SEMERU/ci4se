def systemInformationType6():
    a = L2PseudoLength(l2pLength=11)
    b = TpPd(pd=6)
    c = MessageType(mesType=30)
    d = CellIdentity()
    e = LocalAreaId()
    f = CellOptionsBCCH()
    g = NccPermitted()
    h = Si6RestOctets()
    packet = a / b / c / d / e / f / g
    return packet