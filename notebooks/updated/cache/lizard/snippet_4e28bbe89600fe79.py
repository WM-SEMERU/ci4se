def coverage(args):
    p = OptionParser(coverage.__doc__)
    p.add_option('-c', dest='cutoff', default=0.5, type='float', help=
        'only report query with coverage greater than [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    coordsfile, = args
    fp = open(coordsfile)
    coords = []
    for row in fp:
        try:
            c = CoordsLine(row)
        except AssertionError:
            continue
        coords.append(c)
    coords.sort(key=lambda x: x.query)
    coverages = []
    for query, lines in groupby(coords, key=lambda x: x.query):
        cumulative_cutoff = sum(x.querycov for x in lines)
        coverages.append((query, cumulative_cutoff))
    coverages.sort(key=lambda x: (-x[1], x[0]))
    for query, cumulative_cutoff in coverages:
        if cumulative_cutoff < opts.cutoff:
            break
        print('{0}\t{1:.2f}'.format(query, cumulative_cutoff))