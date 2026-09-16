def pairs(args):
    import jcvi.formats.bed
    p = OptionParser(pairs.__doc__)
    p.set_pairs()
    opts, targs = p.parse_args(args)
    if len(targs) != 1:
        sys.exit(not p.print_help())
    blastfile, = targs
    bedfile = bed([blastfile])
    args[args.index(blastfile)] = bedfile
    return jcvi.formats.bed.pairs(args)