def picard_sam_to_bam(picard, align_sam, fastq_bam, ref_file, is_paired=False):
    to_retain = ['XS', 'XG', 'XM', 'XN', 'XO', 'YT']
    if align_sam.endswith('.sam'):
        out_bam = '%s.bam' % os.path.splitext(align_sam)[0]
    elif align_sam.endswith('-align.bam'):
        out_bam = '%s.bam' % align_sam.replace('-align.bam', '')
    else:
        raise NotImplementedError('Input format not recognized')
    if not file_exists(out_bam):
        with tx_tmpdir(picard._config) as tmp_dir:
            with file_transaction(picard._config, out_bam) as tx_out_bam:
                opts = [('UNMAPPED', fastq_bam), ('ALIGNED', align_sam), (
                    'OUTPUT', tx_out_bam), ('REFERENCE_SEQUENCE', ref_file),
                    ('TMP_DIR', tmp_dir), ('PAIRED_RUN', 'true' if
                    is_paired else 'false')]
                opts += [('ATTRIBUTES_TO_RETAIN', x) for x in to_retain]
                picard.run('MergeBamAlignment', opts)
    return out_bam