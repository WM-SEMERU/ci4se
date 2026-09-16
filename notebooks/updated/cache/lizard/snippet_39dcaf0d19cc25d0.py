def update_from_response(self, response):
    if 'Table' in response:
        self._dict.update(response['Table'])
    elif 'TableDescription' in response:
        self._dict.update(response['TableDescription'])
    if 'KeySchema' in self._dict:
        self._schema = Schema(self._dict['KeySchema'])