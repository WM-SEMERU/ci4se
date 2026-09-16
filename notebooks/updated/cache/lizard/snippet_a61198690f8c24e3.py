def function(self, new_function):
    self._client.change_state(self._monitor_url, {'Monitor[Function]':
        new_function.value})