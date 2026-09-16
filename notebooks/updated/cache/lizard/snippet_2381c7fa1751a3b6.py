def sampe(args, opts):
    dbfile, read1file, read2file = args
    dbfile = check_index(dbfile)
    sai1file = check_aln(dbfile, read1file, cpus=opts.cpus)
    sai2file = check_aln(dbfile, read2file, cpus=opts.cpus)
    samfile, _, unmapped = get_samfile(read1file, dbfile, bam=opts.bam,
        unmapped=opts.unmapped)
    if not need_update((dbfile, sai1file, sai2file), samfile):
        logging.error('`{0}` exists. `bwa samse` already run.'.format(samfile))
        return '', samfile
    cmd = 'bwa sampe ' + ' '.join((dbfile, sai1file, sai2file, read1file,
        read2file))
    cmd += ' ' + opts.extra
    if opts.cutoff:
        cmd += ' -a {0}'.format(opts.cutoff)
    if opts.uniq:
        cmd += ' -n 1'
    return cmd, samfile