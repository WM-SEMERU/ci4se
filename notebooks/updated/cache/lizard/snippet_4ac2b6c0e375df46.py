def apply(self, coordinates):
    for i in self.affected_atoms:
        coordinates[i] = self.transformation * coordinates[i]