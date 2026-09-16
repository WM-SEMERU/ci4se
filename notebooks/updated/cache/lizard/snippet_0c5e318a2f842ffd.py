def cs20(msg):
    chars = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ#####_###############0123456789######'
    d = hex2bin(data(msg))
    cs = ''
    cs += chars[bin2int(d[8:14])]
    cs += chars[bin2int(d[14:20])]
    cs += chars[bin2int(d[20:26])]
    cs += chars[bin2int(d[26:32])]
    cs += chars[bin2int(d[32:38])]
    cs += chars[bin2int(d[38:44])]
    cs += chars[bin2int(d[44:50])]
    cs += chars[bin2int(d[50:56])]
    return cs