def query(self, search_model: QueryModel):
    self.logger.debug('bdb::get::{}'.format(search_model.query))
    assets = json.loads(requests.post('http://localhost:4000/query', data=
        search_model.query).content)['data']
    self.logger.debug('bdb::result::len {}'.format(len(assets)))
    assets_metadata = []
    for i in assets:
        try:
            assets_metadata.append(self._get(i['id'])['data']['data'])
        except:
            pass
    return assets_metadata