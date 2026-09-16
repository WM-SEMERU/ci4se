def geo2apex(self, glat, glon, height):
    glat = helpers.checklat(glat, name='glat')
    alat, alon = self._geo2apex(glat, glon, height)
    if np.any(np.float64(alat) == -9999):
        warnings.warn(
            'Apex latitude set to -9999 where undefined (apex height may be < reference height)'
            )
    return np.float64(alat), np.float64(alon)