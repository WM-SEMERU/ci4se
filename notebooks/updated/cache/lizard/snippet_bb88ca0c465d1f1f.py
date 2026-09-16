def gs50(msg):
    d = hex2bin(data(msg))
    if d[23] == '0':
        return None
    spd = bin2int(d[24:34]) * 2
    return spd