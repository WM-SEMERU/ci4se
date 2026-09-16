def ias53(msg):
    d = hex2bin(data(msg))
    if d[12] == '0':
        return None
    ias = bin2int(d[13:23])
    return ias