def depth(args):
    p = OptionParser(depth.__doc__)
    p.set_outfile()
    opts, args = p.parse_args(args)
    if len(args) != 2:
        sys.exit(not p.print_help())
    readsbed, featsbed = args
    fp = open(featsbed)
    nargs = len(fp.readline().split('\t'))
    keepcols = ','.join(str(x) for x in range(1, nargs + 1))
    cmd = 'coverageBed -a {0} -b {1} -d'.format(readsbed, featsbed)
    cmd += ' | groupBy -g {0} -c {1} -o mean'.format(keepcols, nargs + 2)
    sh(cmd, outfile=opts.outfile)