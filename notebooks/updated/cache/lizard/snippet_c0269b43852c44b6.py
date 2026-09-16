def fuzzy_index_match(possiblities, label, **kwargs):
    possibilities = list(possiblities)
    if isinstance(label, basestring):
        return fuzzy_get(possibilities, label, **kwargs)
    if isinstance(label, int):
        return possibilities[label]
    if isinstance(label, list):
        return [fuzzy_get(possibilities, lbl) for lbl in label]