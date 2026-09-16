def euc_to_python(hexstr):
    hi = hexstr[0:2]
    lo = hexstr[2:4]
    gb_enc = b'\\x' + hi + b'\\x' + lo
    return gb_enc.decode('gb2312')