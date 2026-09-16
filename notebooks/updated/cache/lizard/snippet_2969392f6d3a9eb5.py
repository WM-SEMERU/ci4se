def releaseCompleteMsToNet(Cause_presence=0, Facility_presence=0,
    UserUser_presence=0, SsVersionIndicator_presence=0):
    a = TpPd(pd=3)
    b = MessageType(mesType=42)
    packet = a / b
    if Cause_presence is 1:
        c = CauseHdr(ieiC=8, eightBitC=0)
        packet = packet / c
    if Facility_presence is 1:
        d = FacilityHdr(ieiF=28, eightBitF=0)
        packet = packet / d
    if UserUser_presence is 1:
        e = UserUserHdr(ieiUU=126, eightBitUU=0)
        packet = packet / e
    if SsVersionIndicator_presence is 1:
        f = SsVersionIndicatorHdr(ieiSVI=127, eightBitSVI=0)
        packet = packet / f
    return packet