def vgcsUplinkGrant():
    a = TpPd(pd=6)
    b = MessageType(mesType=9)
    c = RrCause()
    d = RequestReference()
    e = TimingAdvance()
    packet = a / b / c / d / e
    return packet