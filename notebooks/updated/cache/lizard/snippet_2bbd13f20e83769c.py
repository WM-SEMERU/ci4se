def get_rmsd(self, mol1, mol2):
    label1, label2 = self._mapper.uniform_labels(mol1, mol2)
    if label1 is None or label2 is None:
        return float('Inf')
    return self._calc_rms(mol1, mol2, label1, label2)