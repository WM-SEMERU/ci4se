def extend_subj_match_vec(df):
    needs_revcomp = df.sstart > df.send
    add_to_end = df.qlen - df.qend
    add_to_start = df.qstart - 1
    ssum2 = (df.send + df.sstart) / 2.0
    sabs2 = np.abs(df.send - df.sstart) / 2.0
    end_idx = ssum2 + sabs2 - 1
    start_idx = ssum2 - sabs2 - 1
    start_idx[needs_revcomp] -= add_to_end
    start_idx[~needs_revcomp] -= add_to_start
    end_idx[needs_revcomp] += add_to_start
    end_idx[~needs_revcomp] += add_to_end
    clipped_start_idx = np.clip(start_idx, 0, df.slen - 1)
    clipped_end_idx = np.clip(end_idx, 0, df.slen - 1)
    trunc = (clipped_start_idx != start_idx) | (clipped_end_idx != end_idx)
    is_extended = (add_to_start > 0) | (add_to_end > 0)
    return (clipped_start_idx, clipped_end_idx, needs_revcomp, trunc,
        is_extended)