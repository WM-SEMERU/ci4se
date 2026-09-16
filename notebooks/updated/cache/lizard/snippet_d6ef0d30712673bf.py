def get_interested_subsequences(subsequences):
    keep_indices = []
    for subseq in subsequences:
        if subseq == 'all':
            keep_indices.extend([x for x in filter_subseq_suffixes[subseq]])
        else:
            keep_indices.extend([(subseq + '_' + x) for x in
                filter_subseq_suffixes[subseq]])
    return keep_indices