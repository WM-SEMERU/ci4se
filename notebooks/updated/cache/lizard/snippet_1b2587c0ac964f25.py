def supervisor(self):
    supervisor = self._cached_client('supervisor')
    if not self._api_supervisor_session:
        self._api_supervisor_session = self.__create_supervisor_session(
            supervisor)
    return supervisor