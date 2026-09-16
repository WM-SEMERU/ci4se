def copy(self):
    result = Vector3(self.size, self.deriv)
    result.x.v = self.x.v
    result.y.v = self.y.v
    result.z.v = self.z.v
    if self.deriv > 0:
        result.x.d[:] = self.x.d
        result.y.d[:] = self.y.d
        result.z.d[:] = self.z.d
    if self.deriv > 1:
        result.x.dd[:] = self.x.dd
        result.y.dd[:] = self.y.dd
        result.z.dd[:] = self.z.dd
    return result