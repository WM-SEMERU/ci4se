def get_worksheet(self):
    url = self.build_url('')
    q = self.q().select('name').expand('worksheet')
    response = self.session.get(url, params=q.as_params())
    if not response:
        return None
    data = response.json()
    ws = data.get('worksheet')
    if ws is None:
        return None
    return WorkSheet(parent=self.parent, **{self._cloud_data_key: ws})