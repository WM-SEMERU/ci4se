def set_inter_group_bond(self, atom_index_one, atom_index_two, bond_order):
    self.bond_atom_list.append(atom_index_one)
    self.bond_atom_list.append(atom_index_two)
    self.bond_order_list.append(bond_order)