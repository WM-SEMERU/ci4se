def recall(links_true, links_pred=None):
    if _isconfusionmatrix(links_true):
        confusion_matrix = links_true
        v = confusion_matrix[0, 0] / (confusion_matrix[0, 0] +
            confusion_matrix[0, 1])
    else:
        tp = true_positives(links_true, links_pred)
        fn = false_negatives(links_true, links_pred)
        v = tp / (tp + fn)
    return float(v)