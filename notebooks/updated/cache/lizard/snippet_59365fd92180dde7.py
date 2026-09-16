def set_aromatic(self):
    for atom in self.atoms:
        atom.aromatic = 1
    for bond in self.bonds:
        bond.aromatic = 1
        bond.bondorder = 1.5
        bond.bondtype = 4
        bond.symbol = ':'
        bond.fixed = 1
    self.aromatic = 1