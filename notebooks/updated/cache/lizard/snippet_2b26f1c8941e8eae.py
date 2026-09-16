def _search(self, words, include=None, exclude=None, lookup=None):
    lookup = lookup or 'contains'
    query = self.router.worditem.query()
    if include:
        query = query.filter(model_type__in=include)
    if exclude:
        query = query.exclude(model_type__in=include)
    if not words:
        return [query]
    qs = []
    if lookup == 'in':
        qs.append(query.filter(word__in=words))
    elif lookup == 'contains':
        for word in words:
            qs.append(query.filter(word=word))
    else:
        raise ValueError('Unknown lookup "{0}"'.format(lookup))
    return qs