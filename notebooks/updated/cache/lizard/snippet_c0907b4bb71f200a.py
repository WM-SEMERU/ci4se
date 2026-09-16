def grasstruth(args):
    p = OptionParser(grasstruth.__doc__)
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    james, = args
    fp = open(james)
    pairs = set()
    for row in fp:
        atoms = row.split()
        genes = []
        idx = {}
        for i, a in enumerate(atoms):
            aa = a.split('||')
            for ma in aa:
                idx[ma] = i
            genes.extend(aa)
        genes = [x for x in genes if ':' not in x]
        Os = [x for x in genes if x.startswith('Os')]
        for o in Os:
            for g in genes:
                if idx[o] == idx[g]:
                    continue
                pairs.add(tuple(sorted((o, g))))
    for a, b in sorted(pairs):
        print('\t'.join((a, b)))