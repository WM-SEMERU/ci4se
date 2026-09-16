def build_genome_alignment_from_directory(d_name, ref_spec, extensions=None,
    index_exts=None, fail_no_index=False):
    if index_exts is None and fail_no_index:
        raise ValueError(
            'Failure on no index specified for loading genome ' +
            'alignment, but no index extensions specified')
    blocks = []
    for fn in os.listdir(d_name):
        pth = os.path.join(d_name, fn)
        if os.path.isfile(pth):
            _, ext = os.path.splitext(pth)
            if extensions is None or ext in extensions:
                idx_path = __find_index(pth, index_exts)
                if idx_path is None and fail_no_index:
                    raise PyokitIOError('No index file for ' + fn)
                for b in genome_alignment_iterator(pth, ref_spec, idx_path):
                    blocks.append(b)
    return GenomeAlignment(blocks)