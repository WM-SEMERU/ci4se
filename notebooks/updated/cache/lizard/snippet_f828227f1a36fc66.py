def get_custom_fields(self, search=None, start=1, limit=50):
    url = 'rest/api/2/customFields'
    params = {}
    if search:
        params['search'] = search
    if start:
        params['startAt'] = start
    if limit:
        params['maxResults'] = limit
    return self.get(url, params=params)