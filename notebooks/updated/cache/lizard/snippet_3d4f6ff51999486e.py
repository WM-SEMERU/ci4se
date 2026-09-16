def confusion_matrix(links_true, links_pred, total=None):
    links_true = _get_multiindex(links_true)
    links_pred = _get_multiindex(links_pred)
    tp = true_positives(links_true, links_pred)
    fp = false_positives(links_true, links_pred)
    fn = false_negatives(links_true, links_pred)
    if total is None:
        tn = numpy.nan
    else:
        tn = true_negatives(links_true, links_pred, total)
    return numpy.array([[tp, fn], [fp, tn]])