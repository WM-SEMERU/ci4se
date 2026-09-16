def unlock(self):
    if isinstance(self._session, manager.Manager):
        self._session.unlock()