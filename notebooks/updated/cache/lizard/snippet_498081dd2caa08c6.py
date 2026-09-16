def post_collection(self, collection, body):
    assert isinstance(body, list), 'POST requires body to be a list'
    assert collection.startswith('/'), 'Collections must start with /'
    uri = self.uri + '/v1' + collection
    return self.service._post(uri, body)