def _add_atom_info(self, atom_info):
    self.atoms_by_number[atom_info.number] = atom_info
    self.atoms_by_symbol[atom_info.symbol.lower()] = atom_info