def make_scrnaseq_object(samples):
    local_sitelib = R_sitelib()
    counts_dir = os.path.dirname(dd.get_in_samples(samples, dd.
        get_combined_counts))
    gtf_file = dd.get_in_samples(samples, dd.get_transcriptome_gtf)
    if not gtf_file:
        gtf_file = dd.get_in_samples(samples, dd.get_gtf_file)
    rda_file = os.path.join(counts_dir, 'se.rda')
    if not file_exists(rda_file):
        with file_transaction(rda_file) as tx_out_file:
            rcode = '%s-run.R' % os.path.splitext(rda_file)[0]
            rrna_file = '%s-rrna.txt' % os.path.splitext(rda_file)[0]
            rrna_file = _find_rRNA_genes(gtf_file, rrna_file)
            with open(rcode, 'w') as out_handle:
                out_handle.write(_script.format(**locals()))
            rscript = Rscript_cmd()
            try:
                rda_file = rcode
            except subprocess.CalledProcessError as msg:
                logger.exception()