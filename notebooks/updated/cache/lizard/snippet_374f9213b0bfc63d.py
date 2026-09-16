def get_rotations(self):
    if self.centrosymmetric:
        return np.vstack((self.rotations, -self.rotations))
    else:
        return self.rotations