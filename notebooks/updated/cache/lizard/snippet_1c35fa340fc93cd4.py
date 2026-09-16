def f2lookup(f, lookup):
    lookup = {i: r for i, r in [l.strip().split('\t')[0:2] for l in lookup]}
    for line in f:
        line = line.strip().split()
        for i, w in enumerate(line):
            if w in lookup:
                line[i] = lookup[w]
        yield ' '.join(line)