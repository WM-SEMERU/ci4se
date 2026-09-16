def summary(args):
    from jcvi.formats.blast import AlignStats
    p = OptionParser(summary.__doc__)
    p.add_option('-s', dest='single', default=False, action='store_true',
        help='provide stats per reference seq')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(p.print_help())
    coordsfile, = args
    alignstats = get_stats(coordsfile)
    alignstats.print_stats()