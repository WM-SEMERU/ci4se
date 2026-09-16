def activateAaPdpContextRequest(AccessPointName_presence=0,
    ProtocolConfigurationOptions_presence=0, GprsTimer_presence=0):
    a = TpPd(pd=8)
    b = MessageType(mesType=80)
    c = NetworkServiceAccessPointIdentifier()
    d = LlcServiceAccessPointIdentifier()
    e = QualityOfService()
    f = PacketDataProtocolAddress()
    packet = a / b / c / d / e / f
    if AccessPointName_presence is 1:
        g = AccessPointName(ieiAPN=40)
        packet = packet / g
    if ProtocolConfigurationOptions_presence is 1:
        h = ProtocolConfigurationOptions(ieiPCO=39)
        packet = packet / h
    if GprsTimer_presence is 1:
        i = GprsTimer(ieiGT=41)
        packet = packet / i
    return packet