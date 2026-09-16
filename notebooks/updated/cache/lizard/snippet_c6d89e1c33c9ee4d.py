def local_service(self, name_or_id):
    if not self._loop.inside_loop():
        self._state_lock.acquire()
    try:
        if isinstance(name_or_id, int):
            if name_or_id not in self._name_map:
                raise ArgumentError('Unknown ID used to look up service',
                    id=name_or_id)
            name = self._name_map[name_or_id]
        else:
            name = name_or_id
        if name not in self.services:
            raise ArgumentError('Unknown service name', name=name)
        return copy(self.services[name])
    finally:
        if not self._loop.inside_loop():
            self._state_lock.release()