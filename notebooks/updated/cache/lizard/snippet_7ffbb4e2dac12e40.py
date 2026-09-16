def copy(self):
    return GrainBoundary(self.lattice, self.species_and_occu, self.
        frac_coords, self.rotation_axis, self.rotation_angle, self.gb_plane,
        self.join_plane, self.init_cell, self.vacuum_thickness, self.
        ab_shift, self.site_properties, self.oriented_unit_cell)