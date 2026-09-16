def mutation_combinations(mutations):
    mutations = sorted(mutations)
    combntn = itertools.chain.from_iterable(itertools.combinations(
        mutations, x) for x in range(len(mutations) + 1))
    for c in combntn:
        if len(c) > 0:
            positions = [('%s%s' % (m.Chain, m.ResidueID.strip())) for m in c]
            if len(positions) == len(set(positions)):
                yield c