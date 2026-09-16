def projectionpoints(self, pps):
    return [(pp - np.dot(pp - self.p1, self.normal_vector) * self.
        normal_vector) for pp in pps]