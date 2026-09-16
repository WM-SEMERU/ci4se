def __pair_repack(self, f, plist):
    ulist = f(u for p in plist for u in p)
    for u in ulist:
        v = next(ulist)
        yield u, v