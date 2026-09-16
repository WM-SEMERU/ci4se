def generate_adsorption_structures(self, molecule, repeat=None, min_lw=5.0,
    reorient=True, find_args={}):
    if repeat is None:
        xrep = np.ceil(min_lw / np.linalg.norm(self.slab.lattice.matrix[0]))
        yrep = np.ceil(min_lw / np.linalg.norm(self.slab.lattice.matrix[1]))
        repeat = [xrep, yrep, 1]
    structs = []
    for coords in self.find_adsorption_sites(**find_args)['all']:
        structs.append(self.add_adsorbate(molecule, coords, repeat=repeat,
            reorient=reorient))
    return structs