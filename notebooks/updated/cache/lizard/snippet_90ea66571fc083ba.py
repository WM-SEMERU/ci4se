def users(self):
    if self._user_manager is None:
        self._user_manager = UserManager(session=self._session)
    return self._user_manager