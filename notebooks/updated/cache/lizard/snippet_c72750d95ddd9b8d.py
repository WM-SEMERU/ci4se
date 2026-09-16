def _is_reachable(self, server):
    try:
        server['redis'].ping()
        return True
    except UserWarning:
        self._logger.warn('Cannot reach redis server: ' + server['url'])
    except Exception:
        self._logger.warn('Cannot reach redis server: ' + server['url'])
    return False