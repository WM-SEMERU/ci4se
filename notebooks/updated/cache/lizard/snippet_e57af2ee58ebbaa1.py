def packbools(bools, dtype='L'):
    r = NBITS[dtype]
    atoms = ATOMS[dtype]
    for chunk in zip_longest(*([iter(bools)] * r), fillvalue=False):
        yield sum(compress(atoms, chunk))