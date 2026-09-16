def _itodq(self, n):
    if self.v == 4:
        return '.'.join(map(str, [n >> 24 & 255, n >> 16 & 255, n >> 8 & 
            255, n & 255]))
    else:
        n = '%032x' % n
        return ':'.join(n[4 * x:4 * x + 4] for x in range(0, 8))