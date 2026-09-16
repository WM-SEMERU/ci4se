def id_to_atom(self, idx):
    mapped_idx = self.mapid(idx, 'reversed')
    return pybel.Atom(self.original_structure.GetAtom(mapped_idx))