def flatten_dict(self, d, delimiter='-', intermediates=False, parent_key=None):
    items = []
    if isinstance(d, list):
        d = dict(enumerate(d))
    for k, v in d.items():
        if parent_key:
            k = '{}{}{}'.format(parent_key, delimiter, k)
        if intermediates:
            items.append((k, v))
        if isinstance(v, list):
            v = dict(enumerate(v))
        if isinstance(v, collections.Mapping):
            items.extend(self.flatten_dict(v, delimiter, intermediates, str
                (k)).items())
        else:
            items.append((str(k), v))
    return dict(items)