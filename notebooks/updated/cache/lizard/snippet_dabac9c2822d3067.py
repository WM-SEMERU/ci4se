def iterate_intersecting_pairs(layer):
    yielded = set()
    ri = layer[:]
    for i1, elem1 in enumerate(ri):
        for i2, elem2 in enumerate(ri):
            if i1 != i2 and elem1['start'] <= elem2['start'] < elem1['end']:
                inds = (i1, i2) if i1 < i2 else (i2, i1)
                if inds not in yielded and in_by_identity(layer, elem1
                    ) and in_by_identity(layer, elem2):
                    yielded.add(inds)
                    yield elem1, elem2