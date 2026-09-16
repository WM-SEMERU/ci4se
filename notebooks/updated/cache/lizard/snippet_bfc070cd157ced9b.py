def draw_edges(self):
    for e in self.g.E():
        if hasattr(e, 'view'):
            l = []
            r0, r1 = None, None
            if e in self.ctrls:
                D = self.ctrls[e]
                r0, r1 = self.grx[e.v[0]].rank, self.grx[e.v[1]].rank
                if r0 < r1:
                    ranks = xrange(r0 + 1, r1)
                else:
                    ranks = xrange(r0 - 1, r1, -1)
                l = [D[r].view.xy for r in ranks]
            l.insert(0, e.v[0].view.xy)
            l.append(e.v[1].view.xy)
            try:
                self.route_edge(e, l)
            except AttributeError:
                pass
            e.view.setpath(l)