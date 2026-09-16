def get_column(self, id_or_name):
    url = self.build_url(self._endpoints.get('get_column').format(quote(
        id_or_name)))
    response = self.session.get(url)
    if not response:
        return None
    data = response.json()
    return self.column_constructor(parent=self, **{self._cloud_data_key: data})