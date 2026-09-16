def false_positives(links_true, links_pred):
    links_true = _get_multiindex(links_true)
    links_pred = _get_multiindex(links_pred)
    return len(links_pred.difference(links_true))