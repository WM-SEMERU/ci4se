def clear_uservars(self, user=None):
    if user is None:
        self._session.reset_all()
    else:
        self._session.reset(user)