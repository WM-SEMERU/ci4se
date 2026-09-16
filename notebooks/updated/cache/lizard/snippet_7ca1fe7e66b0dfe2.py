def _le_diamond(self, annot, p1, p2, lr):
    m, im, L, R, w, scol, fcol, opacity = self._le_annot_parms(annot, p1, p2)
    shift = 2.5
    d = shift * max(1, w)
    M = R - (d / 2.0, 0) if lr else L + (d / 2.0, 0)
    r = Rect(M, M) + (-d, -d, d, d)
    p = (r.tl + (r.bl - r.tl) * 0.5) * im
    ap = 'q\n%s%f %f m\n' % (opacity, p.x, p.y)
    p = (r.tl + (r.tr - r.tl) * 0.5) * im
    ap += '%f %f l\n' % (p.x, p.y)
    p = (r.tr + (r.br - r.tr) * 0.5) * im
    ap += '%f %f l\n' % (p.x, p.y)
    p = (r.br + (r.bl - r.br) * 0.5) * im
    ap += '%f %f l\n' % (p.x, p.y)
    ap += '%g w\n' % w
    ap += scol + fcol + 'b\nQ\n'
    return ap