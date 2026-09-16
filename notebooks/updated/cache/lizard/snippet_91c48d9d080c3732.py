def zGetSurfaceData(self, surfNum):
    if self.pMode == 0:
        surf_data = _co.namedtuple('surface_data', ['radius', 'thick',
            'material', 'semidia', 'conic', 'comment'])
        surf = self.pLDE.GetSurfaceAt(surfNum)
        return surf_data(surf.pRadius, surf.pThickness, surf.pMaterial,
            surf.pSemiDiameter, surf.pConic, surf.pComment)
    else:
        raise NotImplementedError(
            'Function not implemented for non-sequential mode')