def gap_index_map(sequence, gap_chars='-'):
    return dict((v, k) for k, v in list(ungap_index_map(sequence, gap_chars
        ).items()))