def get_page_labels(self, page_id, prefix=None, start=None, limit=None):
    url = 'rest/api/content/{id}/label'.format(id=page_id)
    params = {}
    if prefix:
        params['prefix'] = prefix
    if start is not None:
        params['start'] = int(start)
    if limit is not None:
        params['limit'] = int(limit)
    return self.get(url, params=params)