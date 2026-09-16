def profileUpperLimit(self, delta=2.71):
    a = self.p_2
    b = self.p_1
    if self.vertex_x < 0:
        c = self.p_0 + delta
    else:
        c = self.p_0 - self.vertex_y + delta
    if b ** 2 - 4.0 * a * c < 0.0:
        print('WARNING')
        print(a, b, c)
        return 0.0
    return max((np.sqrt(b ** 2 - 4.0 * a * c) - b) / (2.0 * a), (-1.0 * np.
        sqrt(b ** 2 - 4.0 * a * c) - b) / (2.0 * a))