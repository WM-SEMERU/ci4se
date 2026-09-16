def notificationNch():
    a = L2PseudoLength(l2pLength=1)
    b = TpPd(pd=6)
    c = MessageType(mesType=32)
    d = NtNRestOctets()
    packet = a / b / c / d
    return packet