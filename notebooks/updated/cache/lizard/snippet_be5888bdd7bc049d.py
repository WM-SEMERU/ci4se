def append(self, species, coords, coords_are_cartesian=False,
    validate_proximity=False, properties=None):
    return self.insert(len(self), species, coords, coords_are_cartesian=
        coords_are_cartesian, validate_proximity=validate_proximity,
        properties=properties)