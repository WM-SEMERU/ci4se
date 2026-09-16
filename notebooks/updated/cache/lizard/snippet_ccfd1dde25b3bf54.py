def __format_filters(filters):
    if filters is not None:
        for k in filters:
            if 'filter[' not in k:
                filters['filter[{}]'.format(k)] = filters.pop(k)
    return filters