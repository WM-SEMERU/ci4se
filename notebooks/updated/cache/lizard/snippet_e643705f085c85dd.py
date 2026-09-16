def dequeue(self):
    if not self.connected:
        raise ConnectionError('Queue is not connected')
    if self.rdb.llen(self._name) == 0:
        return None
    data = self.rdb.rpop(self._name)
    if not data:
        return None
    if isinstance(data, six.binary_type):
        data = six.text_type(data, 'utf-8', errors='replace')
    task = Task()
    task.__dict__ = json.loads(data)
    return task