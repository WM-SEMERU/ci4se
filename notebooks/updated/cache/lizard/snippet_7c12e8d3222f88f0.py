def holdAcknowledge():
    a = TpPd(pd=3)
    b = MessageType(mesType=25)
    packet = a / b
    return packet