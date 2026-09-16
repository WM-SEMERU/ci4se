def trk50(msg):
    d = hex2bin(data(msg))
    if d[11] == '0':
        return None
    sign = int(d[12])
    value = bin2int(d[13:23])
    if sign:
        value = value - 1024
    trk = value * 90.0 / 512.0
    if trk < 0:
        trk = 360 + trk
    return round(trk, 3)