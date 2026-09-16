def pushall(args):
    p = OptionParser(pushall.__doc__)
    opts, args = p.parse_args(args)
    if len(args) < 1:
        sys.exit(not p.print_help())
    flist = args
    for f in flist:
        if f.endswith('.log'):
            continue
        push([f])