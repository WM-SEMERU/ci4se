def rename(self, new_pid):
    logger.info('rename(new_pid="%s") [lid=%s, pid=%s]', new_pid, self.
        __lid, self.__pid)
    evt = self._client._request_point_rename(self._type, self.__lid, self.
        __pid, new_pid)
    self._client._wait_and_except_if_failed(evt)
    self.__pid = new_pid