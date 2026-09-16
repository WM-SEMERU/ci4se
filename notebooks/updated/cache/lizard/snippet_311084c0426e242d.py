def discombobulate(self, filehash):
    idx = [14, 3, 6, 8, 2]
    mul = [2, 2, 5, 4, 3]
    add = [0, 13, 16, 11, 5]
    b = []
    for i in xrange(len(idx)):
        a = add[i]
        m = mul[i]
        i = idx[i]
        t = a + int(filehash[i], 16)
        v = int(filehash[t:t + 2], 16)
        b.append(('%x' % (v * m))[-1])
    return ''.join(b)