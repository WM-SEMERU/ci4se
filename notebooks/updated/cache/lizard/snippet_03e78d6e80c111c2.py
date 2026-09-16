def is_snp(reference_bases, alternate_bases):
    if len(reference_bases) > 1:
        return False
    for alt in alternate_bases:
        if alt is None:
            return False
        if alt not in ['A', 'C', 'G', 'T', 'N', '*']:
            return False
    return True