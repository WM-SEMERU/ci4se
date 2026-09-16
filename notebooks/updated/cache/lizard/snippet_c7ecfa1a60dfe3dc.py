def slide(self, distance):
    distance = float(distance)
    translation = np.eye(4)
    translation[2, 3] = distance
    new_transform = np.dot(self.primitive.transform.copy(), translation.copy())
    self.primitive.transform = new_transform