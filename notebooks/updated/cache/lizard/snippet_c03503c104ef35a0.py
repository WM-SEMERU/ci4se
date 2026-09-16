def findpk2(self, r1, s1, r2, s2, flag1, flag2):
    R1 = self.ec.decompress(r1, flag1)
    R2 = self.ec.decompress(r2, flag2)
    rdiff = self.GFn.value(r1 - r2)
    return (R1 * s1 - R2 * s2) * (1 / rdiff)