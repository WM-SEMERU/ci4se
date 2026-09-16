def _le_ropenarrow(self, annot, p1, p2, lr):
    m, im, L, R, w, scol, fcol, opacity = self._le_annot_parms(annot, p1, p2)
    shift = 2.5
    d = shift * max(1, w)
    p2 = R - (d / 3.0, 0) if lr else L + (d / 3.0, 0)
    p1 = p2 + (2 * d, -d) if lr else p2 + (-2 * d, -d)
    p3 = p2 + (2 * d, d) if lr else p2 + (-2 * d, d)
    p1 *= im
    p2 *= im
    p3 *= im
    ap = '\nq\n%s%f %f m\n' % (opacity, p1.x, p1.y)
    ap += '%f %f l\n' % (p2.x, p2.y)
    ap += '%f %f l\n' % (p3.x, p3.y)
    ap += '%g w\n' % w
    ap += scol + fcol + 'S\nQ\n'
    return ap