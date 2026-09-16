def master_for(self, service):
    if service not in self._masters:
        self._masters[service] = ManagedPool(self, service, is_master=True,
            db=self._redis_db, password=self._redis_password, encoding=self
            ._redis_encoding, minsize=self._redis_minsize, maxsize=self.
            _redis_maxsize, ssl=self._redis_ssl, parser=self._parser_class,
            loop=self._loop)
    return self._masters[service]