def point_to_t(self, point):
    if np.isclose(point, self.start, rtol=0, atol=1e-06):
        return 0.0
    elif np.isclose(point, self.end, rtol=0, atol=1e-06):
        return 1.0
    p = self.poly()
    t = (point - p[0]) / p[1]
    if np.isclose(t.imag, 0) and t.real >= 0.0 and t.real <= 1.0:
        return t.real
    return None