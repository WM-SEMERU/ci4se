def index(args):
    p = OptionParser(index.__doc__)
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(p.print_help())
    frgscffile, = args
    gzfile = frgscffile + '.gz'
    cmd = 'bgzip -c {0}'.format(frgscffile)
    if not op.exists(gzfile):
        sh(cmd, outfile=gzfile)
    tbifile = gzfile + '.tbi'
    cmd = 'tabix -s 2 -b 3 -e 4 {0}'.format(gzfile)
    if not op.exists(tbifile):
        sh(cmd)