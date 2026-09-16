def create_layer(self, lipid_indices=None, flip_orientation=False):
    layer = mb.Compound()
    if not lipid_indices:
        lipid_indices = list(range(self.n_lipids_per_layer))
        shuffle(lipid_indices)
    for n_type, n_of_lipid_type in enumerate(self.
        number_of_each_lipid_per_layer):
        current_type = self.lipids[n_type][0]
        for n_this_type, n_this_lipid_type in enumerate(range(n_of_lipid_type)
            ):
            lipids_placed = n_type + n_this_type
            new_lipid = clone(current_type)
            random_index = lipid_indices[lipids_placed]
            position = self.pattern[random_index]
            particles = list(new_lipid.particles())
            ref_atom = self.ref_atoms[n_type]
            new_lipid.translate(-particles[ref_atom].pos + self.spacing)
            if flip_orientation == True:
                center = new_lipid.center
                center[2] = 0.0
                new_lipid.translate(-center)
                new_lipid.rotate(np.pi, [1, 0, 0])
                new_lipid.translate(center)
            new_lipid.translate(position)
            layer.add(new_lipid)
    return layer, lipid_indices