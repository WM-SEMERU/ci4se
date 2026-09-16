def backbone_bond_lengths(self):
    bond_lengths = dict(n_ca=[distance(r['N'], r['CA']) for r in self.
        get_monomers(ligands=False)], ca_c=[distance(r['CA'], r['C']) for r in
        self.get_monomers(ligands=False)], c_o=[distance(r['C'], r['O']) for
        r in self.get_monomers(ligands=False)], c_n=[distance(r1['C'], r2[
        'N']) for r1, r2 in [(self[i], self[i + 1]) for i in range(len(self
        ) - 1)]])
    return bond_lengths