def count_duplicates(items):
    c = Counter(items)
    return dict((k, v) for k, v in viewitems(c) if v > 1)