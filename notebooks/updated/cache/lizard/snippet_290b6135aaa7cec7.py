def category_filter(self, category_filter):
    allowed_values = ['ADMINISTRATIVE', 'SERVICEHEALTH', 'ALERT',
        'AUTOSCALE', 'SECURITY']
    if not set(category_filter).issubset(set(allowed_values)):
        raise ValueError(
            'Invalid values for `category_filter` [{0}], must be a subset of [{1}]'
            .format(', '.join(map(str, set(category_filter) - set(
            allowed_values))), ', '.join(map(str, allowed_values))))
    self._category_filter = category_filter