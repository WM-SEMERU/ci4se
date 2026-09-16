def flip_strand(self):
    self.reference = complement_alleles(self.reference)
    self.coded = complement_alleles(self.coded)
    self.variant.complement_alleles()