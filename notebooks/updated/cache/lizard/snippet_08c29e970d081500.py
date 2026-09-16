def index(in_bam, config, check_timestamp=True):
    assert is_bam(in_bam), '%s in not a BAM file' % in_bam
    index_file = '%s.bai' % in_bam
    alt_index_file = '%s.bai' % os.path.splitext(in_bam)[0]
    if check_timestamp:
        bai_exists = utils.file_uptodate(index_file, in_bam
            ) or utils.file_uptodate(alt_index_file, in_bam)
    else:
        bai_exists = utils.file_exists(index_file) or utils.file_exists(
            alt_index_file)
    if not bai_exists:
        for fname in [index_file, alt_index_file]:
            utils.remove_safe(fname)
        samtools = config_utils.get_program('samtools', config)
        num_cores = config['algorithm'].get('num_cores', 1)
        with file_transaction(config, index_file) as tx_index_file:
            cmd = '{samtools} index -@ {num_cores} {in_bam} {tx_index_file}'
            do.run(cmd.format(**locals()), 'Index BAM file: %s' % os.path.
                basename(in_bam))
    return index_file if utils.file_exists(index_file) else alt_index_file