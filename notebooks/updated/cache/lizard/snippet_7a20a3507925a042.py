def message(self, message_ids):
    if isinstance(message_ids, list):
        message_ids = ','.join([int(id) for id in message_ids])
    path = '/msg/get/%s' % message_ids
    return self._request(path)