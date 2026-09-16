def qsize(self):
    if not self.connected:
        raise QueueNotConnectedError('Queue is not Connected')
    try:
        size = self.__db.llen(self._key)
    except redis.ConnectionError as e:
        raise redis.ConnectionError(repr(e))
    return size