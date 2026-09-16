def uniq(args):
    from six.moves.urllib.parse import parse_qs
    p = OptionParser(uniq.__doc__)
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    vcffile, = args
    fp = must_open(vcffile)
    data = []
    for row in fp:
        if row[0] == '#':
            print(row.strip())
            continue
        v = VcfLine(row)
        data.append(v)
    for pos, vv in groupby(data, lambda x: x.pos):
        vv = list(vv)
        if len(vv) == 1:
            print(vv[0])
            continue
        bestv = max(vv, key=lambda x: float(parse_qs(x.info)['R2'][0]))
        print(bestv)