def symmetrize_molecule(self):
    eq = self.get_equivalent_atoms()
    eq_sets, ops = eq['eq_sets'], eq['sym_ops']
    coords = self.centered_mol.cart_coords.copy()
    for i, eq_indices in eq_sets.items():
        for j in eq_indices:
            coords[j] = np.dot(ops[j][i], coords[j])
        coords[i] = np.mean(coords[list(eq_indices)], axis=0)
        for j in eq_indices:
            if j == i:
                continue
            coords[j] = np.dot(ops[i][j], coords[i])
            coords[j] = np.dot(ops[i][j], coords[i])
    molecule = Molecule(species=self.centered_mol.species_and_occu, coords=
        coords)
    return {'sym_mol': molecule, 'eq_sets': eq_sets, 'sym_ops': ops}