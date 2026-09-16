def clientCreated(self, *args, **kwargs):
    ref = {'exchange': 'client-created', 'name': 'clientCreated',
        'routingKey': [{'multipleWords': True, 'name': 'reserved'}],
        'schema': 'v1/client-message.json#'}
    return self._makeTopicExchange(ref, *args, **kwargs)