def notificationResponse():
    a = TpPd(pd=6)
    b = MessageType(mesType=38)
    c = MobileStationClassmark2()
    d = MobileId()
    e = DescriptiveGroupOrBroadcastCallReference()
    packet = a / b / c / d / e
    return packet