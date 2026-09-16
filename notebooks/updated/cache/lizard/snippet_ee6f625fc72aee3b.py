def update(self, obj):
    if isinstance(obj, APPMessage):
        self._header = obj._header
        self._payload = obj._payload