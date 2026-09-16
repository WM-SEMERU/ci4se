def plot_model_segments(seg_files, work_dir, data):
    from bcbio.heterogeneity import chromhacks
    out_file = os.path.join(work_dir, '%s.modeled.png' % dd.get_sample_name
        (data))
    if not utils.file_exists(out_file):
        with file_transaction(data, out_file) as tx_out_file:
            dict_file = utils.splitext_plus(dd.get_ref_file(data))[0] + '.dict'
            plot_dict = os.path.join(os.path.dirname(tx_out_file), os.path.
                basename(dict_file))
            with open(dict_file) as in_handle:
                with open(plot_dict, 'w') as out_handle:
                    for line in in_handle:
                        if line.startswith('@SQ'):
                            cur_chrom = [x.split(':', 1)[1].strip() for x in
                                line.split('\t') if x.startswith('SN:')][0]
                            if chromhacks.is_autosomal_or_sex(cur_chrom):
                                out_handle.write(line)
                        else:
                            out_handle.write(line)
            params = ['-T', 'PlotModeledSegments', '--denoised-copy-ratios',
                tz.get_in(['depth', 'bins', 'normalized'], data),
                '--segments', seg_files['final_seg'], '--allelic-counts',
                seg_files['tumor_hets'], '--sequence-dictionary', plot_dict,
                '--minimum-contig-length', '10', '--output-prefix', dd.
                get_sample_name(data), '-O', os.path.dirname(tx_out_file)]
            _run_with_memory_scaling(params, tx_out_file, data)
    return {'seg': out_file}