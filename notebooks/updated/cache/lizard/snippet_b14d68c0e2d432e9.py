def sequence(self):
    seq = [x.mol_code for x in self._monomers]
    return ' '.join(seq)