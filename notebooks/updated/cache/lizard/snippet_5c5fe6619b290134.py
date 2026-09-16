def graftm_package_is_protein(graftm_package):
    found = None
    with open(graftm_package.alignment_hmm_path()) as f:
        r = f.read().split('\n')
    for line in r:
        if line == 'ALPH  DNA':
            found = False
            break
        elif line == 'ALPH  amino':
            found = True
            break
    if found is None:
        raise Exception(
            'Unable to determine whether the HMM was amino acid or dna')
    return found