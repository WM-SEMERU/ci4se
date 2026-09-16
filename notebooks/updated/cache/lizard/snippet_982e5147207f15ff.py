def picard_fixmate(picard, align_bam):
    base, ext = os.path.splitext(align_bam)
    out_file = '%s-sort%s' % (base, ext)
    if not file_exists(out_file):
        with tx_tmpdir(picard._config) as tmp_dir:
            with file_transaction(picard._config, out_file) as tx_out_file:
                opts = [('INPUT', align_bam), ('OUTPUT', tx_out_file), (
                    'TMP_DIR', tmp_dir), ('SORT_ORDER', 'coordinate')]
                picard.run('FixMateInformation', opts)
    return out_file