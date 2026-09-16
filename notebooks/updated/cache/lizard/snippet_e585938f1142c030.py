def take_notification(self, block=True, timeout=None):
    return self._session.take_notification(block, timeout)