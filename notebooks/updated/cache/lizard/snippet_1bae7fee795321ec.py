def get_knownGene_hg19(self):
    if self._knownGene_hg19 is None:
        self._knownGene_hg19 = self._load_knownGene(self.
            _get_path_knownGene_hg19())
    return self._knownGene_hg19