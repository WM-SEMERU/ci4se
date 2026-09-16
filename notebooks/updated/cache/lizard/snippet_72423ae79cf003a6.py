def tas53(msg):
    d = hex2bin(data(msg))
    if d[33] == '0':
        return None
    tas = bin2int(d[34:46]) * 0.5
    return round(tas, 1)