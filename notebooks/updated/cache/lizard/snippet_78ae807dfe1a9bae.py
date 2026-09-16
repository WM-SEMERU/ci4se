def matrix(self):
    result = np.identity(4, float)
    result[0:3, 0:3] = self.r
    return result