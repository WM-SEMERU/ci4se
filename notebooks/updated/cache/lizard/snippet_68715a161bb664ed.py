def routingAreaUpdateComplete(ReceiveNpduNumbersList_presence=0):
    a = TpPd(pd=3)
    b = MessageType(mesType=10)
    packet = a / b
    if ReceiveNpduNumbersList_presence is 1:
        c = ReceiveNpduNumbersList(ieiRNNL=38)
        packet = packet / c
    return packet