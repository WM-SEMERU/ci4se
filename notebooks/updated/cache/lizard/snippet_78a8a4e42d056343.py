def annotation(args):
    from jcvi.formats.base import DictFile
    p = OptionParser(annotation.__doc__)
    p.add_option('--queryids', help=
        'Query IDS file to switch [default: %default]')
    p.add_option('--subjectids', help=
        'Subject IDS file to switch [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    blastfile, = args
    d = '\t'
    qids = DictFile(opts.queryids, delimiter=d) if opts.queryids else None
    sids = DictFile(opts.subjectids, delimiter=d) if opts.subjectids else None
    blast = Blast(blastfile)
    for b in blast:
        query, subject = b.query, b.subject
        if qids:
            query = qids[query]
        if sids:
            subject = sids[subject]
        print('\t'.join((query, subject)))