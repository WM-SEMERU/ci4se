def compute_mga_entropy_stat(mga_vec, codon_pos, stat_func=np.mean,
    default_val=0.0):
    if mga_vec is None:
        return default_val
    myscores = fetch_mga_scores(mga_vec, codon_pos)
    if myscores is not None and len(myscores):
        score_stat = stat_func(myscores)
    else:
        score_stat = default_val
    return score_stat