def sadd(self, key, *members):
    return self._execute([b'SADD', key] + list(members), len(members))