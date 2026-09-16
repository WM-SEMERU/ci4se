def get_rows(self, *, top=None, skip=None):
    url = self.build_url(self._endpoints.get('get_rows'))
    params = {}
    if top is not None:
        params['$top'] = top
    if skip is not None:
        params['$skip'] = skip
    params = None if not params else params
    response = self.session.get(url, params=params)
    if not response:
        return iter(())
    data = response.json()
    return (self.row_constructor(parent=self, **{self._cloud_data_key: row}
        ) for row in data.get('value', []))