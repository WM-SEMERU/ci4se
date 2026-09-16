def fromcsv(args):
    import csv
    from jcvi.formats.sizes import Sizes
    p = OptionParser(fromcsv.__doc__)
    p.add_option('--evidence', default='map', help=
        'Linkage evidence to add in AGP')
    opts, args = p.parse_args(args)
    if len(args) != 3:
        sys.exit(not p.print_help())
    contigsfasta, mapcsv, mapagp = args
    reader = csv.reader(open(mapcsv))
    sizes = Sizes(contigsfasta).mapping
    next(reader)
    fwagp = must_open(mapagp, 'w')
    o = OO()
    for row in reader:
        if len(row) == 2:
            object, ctg = row
            strand = '?'
        elif len(row) == 3:
            object, ctg, strand = row
        size = sizes[ctg]
        o.add(object, ctg, size, strand)
    o.write_AGP(fwagp, gapsize=100, gaptype='scaffold', phases={}, evidence
        =opts.evidence)