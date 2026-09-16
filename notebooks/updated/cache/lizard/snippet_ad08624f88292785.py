def gen(self):
    data_hash = self.get_hash()
    return '{prefix}{hash}'.format(prefix=self._prefix, hash=data_hash)