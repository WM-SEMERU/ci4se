def reload(self, client=None):
    path = self.reload_path
    client = self._require_client(client)
    query_params = {}
    if self.user_project is not None:
        query_params['userProject'] = self.user_project
    self.entities.clear()
    found = client._connection.api_request(method='GET', path=path,
        query_params=query_params)
    self.loaded = True
    for entry in found.get('items', ()):
        self.add_entity(self.entity_from_dict(entry))