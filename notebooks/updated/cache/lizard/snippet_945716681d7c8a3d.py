def iterscan(self, match='*', count=1000):
    if self.serialized:
        return map(lambda x: (self._loads(x[0]), self.cast(x[1])), self.
            _client.zscan_iter(self.key_prefix, match=match, count=count))
    else:
        return map(lambda x: (self._decode(x[0]), self.cast(x[1])), self.
            _client.zscan_iter(self.key_prefix, match=match, count=count))