def orbit_y(self, angle):
    self.position -= self.pivot
    rot = rotation_matrix(-angle, self.b)[:3, :3]
    self.position = np.dot(rot, self.position)
    self.position += self.pivot
    self.a = np.dot(rot, self.a)
    self.b = np.dot(rot, self.b)
    self.c = np.dot(rot, self.c)