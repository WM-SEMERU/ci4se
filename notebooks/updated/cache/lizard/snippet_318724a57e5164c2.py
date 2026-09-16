def _detect_duplicates(bam_file, out_dir, data):
    out_file = os.path.join(out_dir, 'dup_metrics.txt')
    if not utils.file_exists(out_file):
        dup_align_bam = postalign.dedup_bam(bam_file, data)
        logger.info('Detecting duplicates in %s.' % dup_align_bam)
        dup_count = readstats.number_of_mapped_reads(data, dup_align_bam,
            keep_dups=False)
        tot_count = readstats.number_of_mapped_reads(data, dup_align_bam,
            keep_dups=True)
        with file_transaction(data, out_file) as tx_out_file:
            with open(tx_out_file, 'w') as out_handle:
                out_handle.write('%s\n%s\n' % (dup_count, tot_count))
    with open(out_file) as in_handle:
        dupes = float(next(in_handle).strip())
        total = float(next(in_handle).strip())
    if total == 0:
        rate = 'NA'
    else:
        rate = dupes / total
    return {'Duplication Rate of Mapped': rate}