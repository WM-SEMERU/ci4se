def coverage_score(gold, pred, ignore_in_gold=[], ignore_in_pred=[]):
    gold, pred = _preprocess(gold, pred, ignore_in_gold, ignore_in_pred)
    return np.sum(pred != 0) / len(pred)