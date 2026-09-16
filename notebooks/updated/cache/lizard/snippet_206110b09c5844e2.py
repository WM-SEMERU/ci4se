def sort(args):
    p = OptionParser(sort.__doc__)
    p.add_option('--sizes', default=False, action='store_true', help=
        'Sort by decreasing size [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(p.print_help())
    fastafile, = args
    sortedfastafile = fastafile.rsplit('.', 1)[0] + '.sorted.fasta'
    f = Fasta(fastafile, index=False)
    fw = must_open(sortedfastafile, 'w')
    if opts.sizes:
        sortlist = sorted(f.itersizes(), key=lambda x: (-x[1], x[0]))
        logging.debug('Sort by size: max: {0}, min: {1}'.format(sortlist[0],
            sortlist[-1]))
        sortlist = [x for x, s in sortlist]
    else:
        sortlist = sorted(f.iterkeys())
    for key in sortlist:
        rec = f[key]
        SeqIO.write([rec], fw, 'fasta')
    logging.debug('Sorted file written to `{0}`.'.format(sortedfastafile))
    fw.close()
    return sortedfastafile