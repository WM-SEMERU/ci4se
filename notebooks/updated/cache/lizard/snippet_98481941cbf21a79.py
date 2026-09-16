def _calculate_sv_coverage_cnvkit(data, work_dir):
    from bcbio.variation import coverage
    from bcbio.structural import annotate
    out_target_file = os.path.join(work_dir, '%s-target-coverage.cnn' % dd.
        get_sample_name(data))
    out_anti_file = os.path.join(work_dir, '%s-antitarget-coverage.cnn' %
        dd.get_sample_name(data))
    if (not utils.file_exists(out_target_file) or not utils.file_exists(
        out_anti_file)) and (dd.get_align_bam(data) or dd.get_work_bam(data)):
        target_cov = coverage.run_mosdepth(data, 'target', tz.get_in([
            'regions', 'bins', 'target'], data))
        anti_cov = coverage.run_mosdepth(data, 'antitarget', tz.get_in([
            'regions', 'bins', 'antitarget'], data))
        target_cov_genes = annotate.add_genes(target_cov.regions, data,
            max_distance=0)
        out_target_file = _add_log2_depth(target_cov_genes, out_target_file,
            data)
        out_anti_file = _add_log2_depth(anti_cov.regions, out_anti_file, data)
    return out_target_file, out_anti_file