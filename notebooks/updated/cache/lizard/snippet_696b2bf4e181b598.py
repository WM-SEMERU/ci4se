def _rank_init(self, unranked):
    assert self.dag
    scan = {}
    while len(unranked) > 0:
        l = []
        for v in unranked:
            self.setrank(v)
            for e in v.e_out():
                scan[e] = True
            for x in v.N(+1):
                if not False in [scan.get(e, False) for e in x.e_in()]:
                    if x not in l:
                        l.append(x)
        unranked = l