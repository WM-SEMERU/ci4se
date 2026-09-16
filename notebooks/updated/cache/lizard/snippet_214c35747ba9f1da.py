def create(cls, service=Service(), private=False):
    response = service.send(SRequest('POST', cls.path, data={'private':
        private}))
    return cls.from_response(response, service=service)