def rotate_point(self, p):
    p = Quaternion(0, p[0], p[1], p[2], False)
    q1 = self.normalize()
    q2 = self.inverse()
    r = q1 * p * q2
    return r.x, r.y, r.z