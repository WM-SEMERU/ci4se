def get_custom_query(self):
    query = {}
    q = req.get_query()
    if q:
        query['SearchableText'] = q
    path = req.get_path()
    if path:
        query['path'] = {'query': path, 'depth': req.get_depth()}
    recent_created = req.get_recent_created()
    if recent_created:
        date = api.calculate_delta_date(recent_created)
        query['created'] = {'query': date, 'range': 'min'}
    recent_modified = req.get_recent_modified()
    if recent_modified:
        date = api.calculate_delta_date(recent_modified)
        query['modified'] = {'query': date, 'range': 'min'}
    return query