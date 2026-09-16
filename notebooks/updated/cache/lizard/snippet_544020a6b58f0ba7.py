def _handle_get(self, transaction):
    path = str('/' + transaction.request.uri_path)
    transaction.response = Response()
    transaction.response.destination = transaction.request.source
    transaction.response.token = transaction.request.token
    if path == defines.DISCOVERY_URL:
        transaction = self._server.resourceLayer.discover(transaction)
    else:
        try:
            resource = self._server.root[path]
        except KeyError:
            resource = None
        if resource is None or path == '/':
            transaction.response.code = defines.Codes.NOT_FOUND.number
        else:
            transaction.resource = resource
            transaction = self._server.resourceLayer.get_resource(transaction)
    return transaction