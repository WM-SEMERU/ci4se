def pairinplace(args):
    from jcvi.utils.iter import pairwise
    p = OptionParser(pairinplace.__doc__)
    p.add_option('-r', dest='rclip', default=1, type='int', help=
        'pair ID is derived from rstrip N chars [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    fastafile, = args
    base = op.basename(fastafile).split('.')[0]
    frags = base + '.frags.fasta'
    pairs = base + '.pairs.fasta'
    if fastafile.endswith('.gz'):
        frags += '.gz'
        pairs += '.gz'
    fragsfw = must_open(frags, 'w')
    pairsfw = must_open(pairs, 'w')
    N = opts.rclip
    strip_name = lambda x: x[:-N] if N else str
    skipflag = False
    fastaiter = SeqIO.parse(fastafile, 'fasta')
    for a, b in pairwise(fastaiter):
        aid, bid = [strip_name(x) for x in (a.id, b.id)]
        if skipflag:
            skipflag = False
            continue
        if aid == bid:
            SeqIO.write([a, b], pairsfw, 'fasta')
            skipflag = True
        else:
            SeqIO.write([a], fragsfw, 'fasta')
    if not skipflag:
        SeqIO.write([a], fragsfw, 'fasta')
    logging.debug('Reads paired into `%s` and `%s`' % (pairs, frags))