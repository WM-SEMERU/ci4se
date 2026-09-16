def _get_device(self):
    try:
        device = {'name': self._dev.name, 'isReachable': self._dev.
            isReachable, 'isTrusted': self._get_isTrusted()}
    except Exception:
        return None
    return device