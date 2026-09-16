def zadd(self, *args, **kwargs):
    if 'values_callback' not in kwargs:
        kwargs['values_callback'] = self._to_fields
    pieces = fields.SortedSetField.coerce_zadd_args(*args, **kwargs)
    for score, related_field in zip(*([iter(pieces)] * 2)):
        related_method = getattr(related_field, 'zadd')
        related_method(score, self.instance._pk, values_callback=None)