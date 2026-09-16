def get_transformation(self, coordinates):
    atom1, atom2 = self.hinge_atoms
    center = coordinates[atom1]
    axis = coordinates[atom1] - coordinates[atom2]
    axis /= np.linalg.norm(axis)
    angle = np.random.uniform(-self.max_amplitude, self.max_amplitude)
    return Complete.about_axis(center, angle, axis)