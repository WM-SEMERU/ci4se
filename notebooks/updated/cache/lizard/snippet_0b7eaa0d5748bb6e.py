def to_allele_counts(self, max_allele=None, dtype='u1'):
    if max_allele is None:
        max_allele = self.max()
    alleles = list(range(max_allele + 1))
    outshape = self.shape[:-1] + (len(alleles),)
    out = np.zeros(outshape, dtype=dtype)
    for allele in alleles:
        allele_match = self.values == allele
        if self.mask is not None:
            allele_match &= ~self.mask[..., np.newaxis]
        np.sum(allele_match, axis=-1, out=out[..., allele])
    if self.ndim == 2:
        out = GenotypeAlleleCountsVector(out)
    elif self.ndim == 3:
        out = GenotypeAlleleCountsArray(out)
    return out