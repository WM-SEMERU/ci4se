def containing_simplex_and_bcc(self, xi, yi):
    pts = np.column_stack([xi, yi])
    tri = np.empty((pts.shape[0], 3), dtype=np.int)
    bcc = np.empty_like(tri, dtype=np.float)
    for i, pt in enumerate(pts):
        t = _tripack.trfind(3, pt[0], pt[1], self._x, self._y, self.lst,
            self.lptr, self.lend)
        tri[i] = t
        vert = self._points[tri[i] - 1]
        v0 = vert[1] - vert[0]
        v1 = vert[2] - vert[0]
        v2 = pt - vert[0]
        d00 = v0.dot(v0)
        d01 = v0.dot(v1)
        d11 = v1.dot(v1)
        d20 = v2.dot(v0)
        d21 = v2.dot(v1)
        denom = d00 * d11 - d01 * d01
        v = (d11 * d20 - d01 * d21) / denom
        w = (d00 * d21 - d01 * d20) / denom
        u = 1.0 - v - w
        bcc[i] = [u, v, w]
    tri -= 1
    bcc /= bcc.sum(axis=1).reshape(-1, 1)
    return bcc, self._deshuffle_simplices(tri)