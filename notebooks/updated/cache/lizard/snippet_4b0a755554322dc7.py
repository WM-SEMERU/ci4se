def register_service(self, short_name, long_name, allow_duplicate=True):
    self._loop.run_coroutine(self._client.register_service(short_name,
        long_name, allow_duplicate))