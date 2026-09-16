def dump(bqm, fp, vartype_header=False):
    for triplet in _iter_triplets(bqm, vartype_header):
        fp.write('%s\n' % triplet)