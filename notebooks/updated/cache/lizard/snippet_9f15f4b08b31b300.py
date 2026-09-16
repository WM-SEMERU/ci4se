def maf(genotypes):
    warnings.warn("deprecated: use 'Genotypes.maf'", DeprecationWarning)
    g = genotypes.genotypes
    maf = np.nansum(g) / (2 * np.sum(~np.isnan(g)))
    if maf > 0.5:
        maf = 1 - maf
        return maf, False
    return maf, True