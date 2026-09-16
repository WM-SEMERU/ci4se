def run(self, **client_params):
    try:
        self.send(self.get_collection_endpoint(), http_method='POST', **
            client_params)
    except Exception as e:
        raise CartoException(e)