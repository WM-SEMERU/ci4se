def _keys(self, pattern):
    result = []
    for client in self.redis_clients:
        result.extend(list(client.scan_iter(match=pattern)))
    return result