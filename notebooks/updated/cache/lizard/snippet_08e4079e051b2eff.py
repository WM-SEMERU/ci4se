def _get_filter_ids(cls, request):
    id_query = request.url.query.get('id', None)
    if id_query is None:
        return None
    filter_ids = id_query.split(',')
    for filter_id in filter_ids:
        cls._validate_id(filter_id)
    return filter_ids