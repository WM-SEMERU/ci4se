def relabel_non_zero(label_image, start=1):
    r
    if start <= 0:
        raise ArgumentError('The starting value can not be 0 or lower.')
    l = list(scipy.unique(label_image))
    if 0 in l:
        l.remove(0)
    mapping = dict()
    mapping[0] = 0
    for key, item in zip(l, list(range(start, len(l) + start))):
        mapping[key] = item
    return relabel_map(label_image, mapping)