def apex2geo(self, alat, alon, height, precision=1e-10):
    alat = helpers.checklat(alat, name='alat')
    qlat, qlon = self.apex2qd(alat, alon, height=height)
    glat, glon, error = self.qd2geo(qlat, qlon, height, precision=precision)
    return glat, glon, error