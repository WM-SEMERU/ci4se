def without(seq1, seq2):
    r
    if isSet(seq2):
        d2 = seq2
    else:
        d2 = set(seq2)
    return [elt for elt in seq1 if elt not in d2]