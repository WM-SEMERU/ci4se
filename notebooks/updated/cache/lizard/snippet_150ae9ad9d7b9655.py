def surface(cls, predstr):
    lemma, pos, sense, _ = split_pred_string(predstr)
    return cls(Pred.SURFACE, lemma, pos, sense, predstr)