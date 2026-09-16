def frombed(args):
    p = OptionParser(frombed.__doc__)
    p.add_option('--type', default='match', help=
        'GFF feature type [default: %default]')
    p.add_option('--source', default='default', help=
        'GFF source qualifier [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    bedfile, = args
    bed = Bed(bedfile)
    for b in bed:
        print(b.gffline(type=opts.type, source=opts.source))