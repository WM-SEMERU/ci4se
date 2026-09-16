def load_rdkit_mol(self, mol):
    self.system = {'elements': np.empty(mol.GetNumAtoms(), dtype=str),
        'coordinates': np.empty((mol.GetNumAtoms(), 3))}
    for atom in mol.GetAtoms():
        atom_id = atom.GetIdx()
        atom_sym = atom.GetSymbol()
        x, y, z = mol.GetConformer().GetAtomPosition(atom_id)
        self.system['elements'][atom_id] = atom_sym
        self.system['coordinates'][atom_id] = x, y, z
    return self.system