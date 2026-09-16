def prepare(args):
    try:
        f = open(args.config, 'r')
        seq_out = open(op.join(args.out, 'seqs.fastq'), 'w')
        ma_out = open(op.join(args.out, 'seqs.ma'), 'w')
    except IOError as e:
        traceback.print_exc()
        raise IOError('Can not create output files: %s, %s or read %s' % (
            op.join(args.out, 'seqs.ma'), op.join(args.out, 'seqs.fastq'),
            args.config))
    logger.info('Reading sequeces')
    seq_l, sample_l = _read_fastq_files(f, args)
    logger.info('Creating matrix with unique sequences')
    logger.info(
        'Filtering: min counts %s, min size %s, max size %s, min shared %s' %
        (args.minc, args.minl, args.maxl, args.min_shared))
    _create_matrix_uniq_seq(sample_l, seq_l, ma_out, seq_out, args.min_shared)
    logger.info(
        'Finish preprocessing. Get a sorted BAM file of seqs.fa and run seqcluster cluster.'
        )