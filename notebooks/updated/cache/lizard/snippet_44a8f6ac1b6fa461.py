def fcs(args):
    p = OptionParser(fcs.__doc__)
    p.add_option('--cutoff', default=200, help=
        'Skip small components less than [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    fcsfile, = args
    cutoff = opts.cutoff
    fp = open(fcsfile)
    for row in fp:
        if row[0] == '#':
            continue
        sep = '\t' if '\t' in row else None
        atoms = row.rstrip().split(sep, 3)
        contig, length = atoms[:2]
        length = int(length)
        label = atoms[-1]
        label = label.replace(' ', '_')
        if len(atoms) == 3:
            ranges = '{0}..{1}'.format(1, length)
        else:
            assert len(atoms) == 4
            ranges = atoms[2]
        for ab in ranges.split(','):
            a, b = ab.split('..')
            a, b = int(a), int(b)
            assert a <= b
            ahang = a - 1
            bhang = length - b
            if ahang < cutoff:
                a = 1
            if bhang < cutoff:
                b = length
            print('\t'.join(str(x) for x in (contig, a - 1, b, label)))