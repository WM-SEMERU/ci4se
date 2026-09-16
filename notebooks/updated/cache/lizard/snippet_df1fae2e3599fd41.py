def s2b(s):
    ret = []
    for c in s:
        ret.append(bin(ord(c))[2:].zfill(8))
    return ''.join(ret)