def no_gaps(curve):
    tnt = utils.top_and_tail(curve)
    return not any(np.isnan(tnt))