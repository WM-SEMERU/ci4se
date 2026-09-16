def get_sampleEdge(self, res, DS=None, resMode='abs', offsetIn=0.0):
    pts, dlr, ind = _comp._Ves_get_sampleEdge(self.Poly, res, DS=DS, dLMode
        =resMode, DIn=offsetIn, VIn=self.dgeom['VIn'], margin=1e-09)
    return pts, dlr, ind