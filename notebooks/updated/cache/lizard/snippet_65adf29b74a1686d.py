async def was_killed(self, container_id):
    if container_id in self._watching:
        self._watching.remove(container_id)
    if container_id in self._container_had_error:
        self._container_had_error.remove(container_id)
        return 'timeout'
    return None