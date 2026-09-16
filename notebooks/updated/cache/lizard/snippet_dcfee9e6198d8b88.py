def users(self):
    if self._users is None:
        self._users = UserList(self._version, service_sid=self._solution['sid']
            )
    return self._users