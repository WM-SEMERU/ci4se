def build(args):
    p = OptionParser(build.__doc__)
    p.add_option('--newagp', dest='newagp', default=False, action=
        'store_true', help=
        "Check components to trim dangling N's [default: %default]")
    p.add_option('--novalidate', dest='novalidate', default=False, action=
        'store_true', help="Don't validate the agpfile [default: %default]")
    opts, args = p.parse_args(args)
    if len(args) != 3:
        sys.exit(not p.print_help())
    agpfile, componentfasta, targetfasta = args
    validate = not opts.novalidate
    if opts.newagp:
        assert agpfile.endswith('.agp')
        newagpfile = agpfile.replace('.agp', '.trimmed.agp')
        newagp = open(newagpfile, 'w')
    else:
        newagpfile = None
        newagp = None
    agp = AGP(agpfile, validate=validate, sorted=True)
    agp.build_all(componentfasta=componentfasta, targetfasta=targetfasta,
        newagp=newagp)
    logging.debug('Target fasta written to `{0}`.'.format(targetfasta))
    return newagpfile