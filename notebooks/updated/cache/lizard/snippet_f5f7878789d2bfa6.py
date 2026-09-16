def create(self, item, **kwargs):
    response = self._new_response()
    if self._prototype_handler.check(item, 'create', response):
        self._encrypt(item)
        params = {'Item': item}
        self._call_ddb_method(self.table.put_item, params, response)
        if response.status == 'success':
            response.data = item
    response.prepare()
    return response