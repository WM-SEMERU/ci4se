def get_probs(data, prob_column=None):
    if prob_column is None:
        p = None
    else:
        p = data[prob_column].fillna(0).values
        if p.sum() == 0:
            p = np.ones(len(p))
        if abs(p.sum() - 1.0) > 1e-08:
            p = p / (1.0 * p.sum())
    return p