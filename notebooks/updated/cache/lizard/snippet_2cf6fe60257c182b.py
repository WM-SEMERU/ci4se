def systemInformationType16():
    a = L2PseudoLength(l2pLength=1)
    b = TpPd(pd=6)
    c = MessageType(mesType=61)
    d = Si16RestOctets()
    packet = a / b / c / d
    return packet