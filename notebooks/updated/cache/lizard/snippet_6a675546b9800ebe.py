def _filter_by_normal(tumor_counts, normal_counts, data):
    from bcbio.heterogeneity import bubbletree
    fparams = bubbletree.NORMAL_FILTER_PARAMS
    tumor_out = '%s-normfilter%s' % utils.splitext_plus(tumor_counts)
    normal_out = '%s-normfilter%s' % utils.splitext_plus(normal_counts)
    if not utils.file_uptodate(tumor_out, tumor_counts):
        with file_transaction(data, tumor_out, normal_out) as (tx_tumor_out,
            tx_normal_out):
            median_depth = _get_normal_median_depth(normal_counts)
            min_normal_depth = median_depth * fparams['min_depth_percent']
            max_normal_depth = median_depth * fparams['max_depth_percent']
            with open(tumor_counts) as tumor_handle:
                with open(normal_counts) as normal_handle:
                    with open(tx_tumor_out, 'w') as tumor_out_handle:
                        with open(tx_normal_out, 'w') as normal_out_handle:
                            header = None
                            for t, n in zip(tumor_handle, normal_handle):
                                if header is None:
                                    if not n.startswith('@'):
                                        header = n.strip().split()
                                    tumor_out_handle.write(t)
                                    normal_out_handle.write(n)
                                elif _normal_passes_depth(header, n,
                                    min_normal_depth, max_normal_depth
                                    ) and _normal_passes_freq(header, n,
                                    fparams):
                                    tumor_out_handle.write(t)
                                    normal_out_handle.write(n)
    return tumor_out, normal_out