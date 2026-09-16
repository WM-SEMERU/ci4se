def kmcop(args):
    p = OptionParser(kmcop.__doc__)
    p.add_option('--action', choices=('union', 'intersect'), default=
        'union', help='Action')
    p.add_option('-o', default='results', help='Output name')
    opts, args = p.parse_args(args)
    if len(args) < 2:
        sys.exit(not p.print_help())
    indices = args
    ku = KMCComplex(indices)
    ku.write(opts.o, action=opts.action)