def list_commands(self, page_size=None):
    params = {}
    if page_size is not None:
        params['limit'] = page_size
    return pagination.Iterator(client=self._client, path='/mdb/{}/commands'
        .format(self._instance), params=params, response_class=mdb_pb2.
        ListCommandsResponse, items_key='command', item_mapper=Command)