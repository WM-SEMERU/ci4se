def deactivatePdpContextAccept():
    a = TpPd(pd=8)
    b = MessageType(mesType=71)
    packet = a / b
    return packet