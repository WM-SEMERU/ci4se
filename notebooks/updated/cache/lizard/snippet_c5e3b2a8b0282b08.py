def delete(cls, id):
    client = cls._new_api_client()
    return client.make_request(cls, 'delete', url_params={'id': id})