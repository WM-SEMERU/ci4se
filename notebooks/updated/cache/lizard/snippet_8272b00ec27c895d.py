def _get_container_state(self):
    try:
        result = yield from self.manager.query('GET', 'containers/{}/json'.
            format(self._cid))
    except DockerError:
        return 'exited'
    if result['State']['Paused']:
        return 'paused'
    if result['State']['Running']:
        return 'running'
    return 'exited'