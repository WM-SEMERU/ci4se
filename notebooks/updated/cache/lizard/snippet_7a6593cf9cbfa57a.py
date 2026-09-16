def filterm4(args):
    p = OptionParser(filterm4.__doc__)
    p.add_option('--best', default=1, type='int', help=
        'Only retain best N hits')
    p.set_outfile()
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    m4file, = args
    best = opts.best
    fp = open(m4file)
    fw = must_open(opts.outfile, 'w')
    seen = defaultdict(int)
    retained = total = 0
    for row in fp:
        r = M4Line(row)
        total += 1
        if total % 100000 == 0:
            logging.debug('Retained {0} lines'.format(percentage(retained,
                total)))
        if seen.get(r.query, 0) < best:
            fw.write(row)
            seen[r.query] += 1
            retained += 1
    fw.close()