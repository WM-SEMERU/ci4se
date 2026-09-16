def tidy(args):
    p = OptionParser(tidy.__doc__)
    p.add_option('--gapsize', dest='gapsize', default=0, type='int', help=
        'Set all gaps to the same size [default: %default]')
    p.add_option('--minlen', dest='minlen', default=100, type='int', help=
        'Minimum component size [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    fastafile, = args
    gapsize = opts.gapsize
    minlen = opts.minlen
    tidyfastafile = fastafile.rsplit('.', 1)[0] + '.tidy.fasta'
    fw = must_open(tidyfastafile, 'w')
    removed = normalized = 0
    fasta = Fasta(fastafile, lazy=True)
    for name, rec in fasta.iteritems_ordered():
        rec.seq = rec.seq.upper()
        if minlen:
            removed += remove_small_components(rec, minlen)
        trim_terminal_Ns(rec)
        if gapsize:
            normalized += normalize_gaps(rec, gapsize)
        if len(rec) == 0:
            logging.debug('Drop seq {0}'.format(rec.id))
            continue
        SeqIO.write([rec], fw, 'fasta')
    if removed:
        logging.debug('Total discarded bases: {0}'.format(removed))
    if normalized:
        logging.debug('Gaps normalized: {0}'.format(normalized))
    logging.debug('Tidy FASTA written to `{0}`.'.format(tidyfastafile))
    fw.close()
    return tidyfastafile