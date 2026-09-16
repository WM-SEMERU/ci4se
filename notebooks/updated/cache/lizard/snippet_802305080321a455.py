def stream(self, callback=None):
    if callback is None:
        callback = Response.__default
    if not callable(callback):
        raise Exception('callback must be callable')
    queue = 'stream:%s' % self.id
    r = self._client._redis
    while True:
        data = r.blpop(queue, 10)
        if data is None:
            if not self.running:
                break
            continue
        _, body = data
        payload = json.loads(body.decode())
        message = payload['message']
        line = message['message']
        meta = message['meta']
        callback(meta >> 16, line, meta & 255)
        if meta & 6 != 0:
            break