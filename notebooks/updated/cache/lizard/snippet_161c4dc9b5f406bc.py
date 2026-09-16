def to_dict(self, fields=_all_fields, labels=None):
    fields = set(fields)
    diff = fields.difference(_all_fields)
    if isinstance(labels, Sequence):
        labels = _map_labels(self, labels)
    elif labels is None:
        labels = {}
    if diff:
        raise ValueError('Invalid field(s): {}'.format(', '.join(diff)))
    return _to_dict(self, fields, labels)