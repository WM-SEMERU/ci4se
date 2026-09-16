def rezero(self):
    dimension = self.vertices.shape[1]
    matrix = np.eye(dimension + 1)
    matrix[:dimension, (dimension)] = -self.vertices.min(axis=0)
    self.apply_transform(matrix)
    return matrix