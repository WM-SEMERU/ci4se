def _setup_reference_files(data, tx_out_dir):
    aligner = dd.get_aligner(data) or 'bwa'
    out_dir = utils.safe_makedir(os.path.join(tx_out_dir, aligner))
    ref_fasta = dd.get_ref_file(data)
    ref_files = [('%s%s' % (utils.splitext_plus(ref_fasta)[0], ext)) for
        ext in ['.fa', '.fa.fai', '.dict']]
    for orig_file in (ref_files + tz.get_in(('reference', aligner,
        'indexes'), data)):
        utils.symlink_plus(orig_file, os.path.join(out_dir, os.path.
            basename(orig_file)))
    return os.path.join(out_dir, os.path.basename(ref_fasta))