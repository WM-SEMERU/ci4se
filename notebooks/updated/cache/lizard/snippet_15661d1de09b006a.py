def get_zmat(self, construction_table=None, use_lookup=None):
    if use_lookup is None:
        use_lookup = settings['defaults']['use_lookup']
    self.get_bonds(use_lookup=use_lookup)
    self._give_val_sorted_bond_dict(use_lookup=use_lookup)
    use_lookup = True
    if construction_table is None:
        c_table = self.get_construction_table(use_lookup=use_lookup)
        c_table = self.correct_dihedral(c_table, use_lookup=use_lookup)
        c_table = self.correct_absolute_refs(c_table)
    else:
        c_table = construction_table
    return self._build_zmat(c_table)