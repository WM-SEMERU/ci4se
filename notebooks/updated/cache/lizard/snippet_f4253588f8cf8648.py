def qd2apex(self, qlat, qlon, height):
    alat, alon = self._qd2apex(qlat, qlon, height)
    return np.float64(alat), np.float64(alon)