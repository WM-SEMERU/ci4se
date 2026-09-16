def auc(truth, recommend):
    tp = correct = 0.0
    for r in recommend:
        if r in truth:
            tp += 1.0
        else:
            correct += tp
    pairs = tp * (recommend.size - tp)
    if pairs == 0:
        return 0.5
    return correct / pairs