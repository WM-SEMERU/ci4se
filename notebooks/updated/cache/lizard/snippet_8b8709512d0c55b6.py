def code_minor(genotypes):
    warnings.warn("deprecated: use 'Genotypes.code_minor'", DeprecationWarning)
    _, minor_coded = maf(genotypes)
    if not minor_coded:
        return flip_alleles(genotypes)
    return genotypes