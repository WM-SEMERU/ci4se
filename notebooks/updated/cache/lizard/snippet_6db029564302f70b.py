def get_charge_transfer(self, atom_index):
    if self.potcar is None:
        raise ValueError(
            'POTCAR must be supplied in order to calculate charge transfer!')
    potcar_indices = []
    for i, v in enumerate(self.natoms):
        potcar_indices += [i] * v
    nelect = self.potcar[potcar_indices[atom_index]].nelectrons
    return self.data[atom_index]['charge'] - nelect