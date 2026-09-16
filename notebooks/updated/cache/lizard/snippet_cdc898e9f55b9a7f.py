def dotted(self):
    v = str(self.geoid.tract).zfill(6)
    return v[0:4] + '.' + v[4:]