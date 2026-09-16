def publish(self, payload):
    if self._serializer is not None:
        payload = self._serializer(payload)
    if self._topic == '*':
        msg = payload
    else:
        msg = '{topic} {data}'.format(topic=self._topic, data=payload)
    self._socket.send(cast_bytes(msg))