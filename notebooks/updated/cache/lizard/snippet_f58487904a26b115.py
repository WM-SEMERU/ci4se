def process_params(request, standard_params=STANDARD_QUERY_PARAMS,
    filter_fields=None, defaults=None):
    if not filter_fields:
        filter_fields = []
    unfilterable = set(request.query.keys()) - set(filter_fields) - set(
        standard_params)
    if unfilterable:
        bottle.abort(400, 
            'The following query params were invalid: %s. Try one (or more) of %s.'
             % (', '.join(unfilterable), ', '.join(filter_fields)))
    query_fields = defaults or {}
    for key in request.query:
        if key in filter_fields:
            matches = request.query.getall(key)
            matches = list(itertools.chain(*(k.split(',') for k in matches)))
            if len(matches) > 1:
                query_fields[key] = matches
            else:
                query_fields[key] = matches[0]
    if 'sort' in request.query:
        sort = request.query.getall('sort')
        sort = list(itertools.chain(*(comma_separated_strings(str(k)) for k in
            sort)))
        query_fields['sort'] = sort
    if 'q' in request.query:
        search = request.query.getall('q')
        search = list(itertools.chain(*(comma_separated_strings(k) for k in
            search if k)))
        query_fields['q'] = search
    return query_fields