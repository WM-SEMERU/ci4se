def detachRequest(GmmCause_presence=0):
    a = TpPd(pd=3)
    b = MessageType(mesType=5)
    c = DetachTypeAndForceToStandby()
    packet = a / b / c
    if GmmCause_presence is 1:
        e = GmmCause(ieiGC=37)
        packet = packet / e
    return packet