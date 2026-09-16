def mergebed(args):
    p = OptionParser(mergebed.__doc__)
    p.add_option('-w', '--weightsfile', default='weights.txt', help=
        'Write weights to file')
    p.set_outfile('out.bed')
    opts, args = p.parse_args(args)
    if len(args) < 1:
        sys.exit(not p.print_help())
    maps = args
    outfile = opts.outfile
    fp = must_open(maps)
    b = Bed()
    mapnames = set()
    for row in fp:
        mapname = filename_to_mapname(fp.filename())
        mapnames.add(mapname)
        try:
            m = BedLine(row)
            m.accn = '{0}-{1}'.format(mapname, m.accn)
            m.extra = ['{0}:{1}'.format(m.seqid, m.start)]
            b.append(m)
        except (IndexError, ValueError):
            continue
    b.print_to_file(filename=outfile, sorted=True)
    logging.debug('A total of {0} markers written to `{1}`.'.format(len(b),
        outfile))
    assert len(maps) == len(mapnames), 'You have a collision in map names'
    write_weightsfile(mapnames, weightsfile=opts.weightsfile)