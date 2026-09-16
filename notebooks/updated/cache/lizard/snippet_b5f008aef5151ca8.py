def ignore(self, tube):
    with self._sock_ctx() as socket:
        if tube not in self._watchlist:
            raise KeyError(tube)
        if tube != 'default':
            self.desired_watchlist.remove(tube)
        if tube in self._watchlist:
            self._send_message('ignore {0}'.format(tube), socket)
            self._receive_id(socket)
            self._watchlist.remove(tube)
        if not self._watchlist:
            self._watchlist.add('default')