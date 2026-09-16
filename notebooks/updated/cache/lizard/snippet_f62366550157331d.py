def attachAccept(PTmsiSignature_presence=0, GprsTimer_presence=0,
    MobileId_presence=0, MobileId_presence1=0, GmmCause_presence=0):
    a = TpPd(pd=3)
    b = MessageType(mesType=2)
    c = AttachResult()
    d = ForceToStandby()
    e = GprsTimer()
    f = RadioPriorityAndSpareHalfOctets()
    h = RoutingAreaIdentification()
    packet = a / b / c / d / e / f / h
    if PTmsiSignature_presence is 1:
        i = PTmsiSignature(ieiPTS=25)
        packet = packet / i
    if GprsTimer_presence is 1:
        j = GprsTimer(ieiGT=23)
        packet = packet / j
    if MobileId_presence is 1:
        k = MobileIdHdr(ieiMI=24, eightBitMI=0)
        packet = packet / k
    if MobileId_presence1 is 1:
        l = MobileIdHdr(ieiMI=35, eightBitMI=0)
        packet = packet / l
    if GmmCause_presence is 1:
        m = GmmCause(ieiGC=37)
        packet = packet / m
    return packet