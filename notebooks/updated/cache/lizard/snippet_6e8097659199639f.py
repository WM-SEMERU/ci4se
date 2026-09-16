def load(klass, client, id, **kwargs):
    resource = klass.RESOURCE.format(id=id)
    response = Request(client, 'get', resource, params=kwargs).perform()
    return klass(client).from_response(response.body['data'])