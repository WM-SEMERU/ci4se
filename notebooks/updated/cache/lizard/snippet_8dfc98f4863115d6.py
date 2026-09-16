def idcode(msg):
    if df(msg) not in [5, 21]:
        raise RuntimeError('Message must be Downlink Format 5 or 21.')
    mbin = hex2bin(msg)
    C1 = mbin[19]
    A1 = mbin[20]
    C2 = mbin[21]
    A2 = mbin[22]
    C4 = mbin[23]
    A4 = mbin[24]
    B1 = mbin[26]
    D1 = mbin[27]
    B2 = mbin[28]
    D2 = mbin[29]
    B4 = mbin[30]
    D4 = mbin[31]
    byte1 = int(A4 + A2 + A1, 2)
    byte2 = int(B4 + B2 + B1, 2)
    byte3 = int(C4 + C2 + C1, 2)
    byte4 = int(D4 + D2 + D1, 2)
    return str(byte1) + str(byte2) + str(byte3) + str(byte4)