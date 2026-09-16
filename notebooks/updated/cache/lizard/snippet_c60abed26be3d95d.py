def delt(self, dst, gw=None):
    tmp = dst + b'/128'
    dst, plen = tmp.split(b'/')[:2]
    dst = in6_ptop(dst)
    plen = int(plen)
    l = [x for x in self.routes if in6_ptop(x[0]) == dst and x[1] == plen]
    if gw:
        gw = in6_ptop(gw)
        l = [x for x in self.routes if in6_ptop(x[0]) == gw]
    if len(l) == 0:
        warning('No matching route found')
    elif len(l) > 1:
        warning('Found more than one match. Aborting.')
    else:
        i = self.routes.index(l[0])
        self.invalidate_cache()
        del self.routes[i]