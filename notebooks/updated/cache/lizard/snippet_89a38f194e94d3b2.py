def _get_purecn_files(paired, work_dir, require_exist=False):
    out_base = os.path.join(work_dir, '%s-purecn' % dd.get_sample_name(
        paired.tumor_data))
    out = {'plot': {}}
    all_files = []
    for plot in ['chromosomes', 'local_optima', 'segmentation', 'summary']:
        if plot == 'summary':
            cur_file = '%s.pdf' % out_base
        else:
            cur_file = '%s_%s.pdf' % (out_base, plot)
        if not require_exist or os.path.exists(cur_file):
            out['plot'][plot] = cur_file
            all_files.append(os.path.basename(cur_file))
    for key, ext in [['hetsummary', '.csv'], ['dnacopy', '_dnacopy.seg'], [
        'genes', '_genes.csv'], ['log', '.log'], ['loh', '_loh.csv'], [
        'rds', '.rds'], ['variants', '_variants.csv']]:
        cur_file = '%s%s' % (out_base, ext)
        if not require_exist or os.path.exists(cur_file):
            out[key] = cur_file
            all_files.append(os.path.basename(cur_file))
    return out_base, out, all_files