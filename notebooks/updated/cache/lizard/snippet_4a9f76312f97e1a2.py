def gc3(args):
    p = OptionParser(gc3.__doc__)
    p.add_option('--plot', default=False, action='store_true', help=
        'Also plot the GC3 histogram [default: %default]')
    p.set_outfile()
    opts, args = p.parse_args(args)
    outfile = opts.outfile
    plot = opts.plot
    if not 1 < len(args) < 4:
        sys.exit(not p.print_help())
    ks_file, cdsfile = args[:2]
    GC3 = get_GC3(cdsfile)
    if plot:
        plot_GC3(GC3, cdsfile, fill='green')
    if len(args) == 3:
        cdsfile2 = args[2]
        GC3_2 = get_GC3(cdsfile2)
        GC3.update(GC3_2)
        if plot:
            plot_GC3(GC3_2, cdsfile2, fill='lightgreen')
    data = KsFile(ks_file)
    noriginals = len(data)
    fw = must_open(outfile, 'w')
    writer = csv.writer(fw)
    writer.writerow(fields.split(','))
    nlines = 0
    cutoff = 0.75
    for d in data:
        a, b = d.name.split(';')
        aratio, bratio = GC3[a], GC3[b]
        if (aratio + bratio) / 2 > cutoff:
            continue
        writer.writerow(d)
        nlines += 1
    logging.debug('{0} records written (from {1}).'.format(nlines, noriginals))