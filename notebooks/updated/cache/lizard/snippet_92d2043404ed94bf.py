def service_info(self, name):
    return self._loop.run_coroutine(self._client.service_info(name))