def fixpairs(args):
    p = OptionParser(fixpairs.__doc__)
    opts, args = p.parse_args(args)
    if len(args) != 3:
        sys.exit(not p.print_help())
    pairsfile, sep, sd = args
    newpairsfile = pairsfile.rsplit('.', 1)[0] + '.new.pairs'
    sep = int(sep)
    sd = int(sd)
    p = PairsFile(pairsfile)
    p.fixLibraryStats(sep, sd)
    p.write(newpairsfile)