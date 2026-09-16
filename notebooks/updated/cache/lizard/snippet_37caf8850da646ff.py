def apply_transform(self, matrix):
    matrix = np.asanyarray(matrix, dtype=np.float64)
    if matrix.shape != (4, 4):
        raise ValueError('shape must be 4,4')
    center = np.dot(matrix, np.append(self.primitive.center, 1.0))[:3]
    self.primitive.center = center