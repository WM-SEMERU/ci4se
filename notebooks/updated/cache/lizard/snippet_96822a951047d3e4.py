def _select_next_server(self):
    while True:
        if len(self._server_pool) == 0:
            self._current_server = None
            raise ErrNoServers
        now = time.time()
        s = self._server_pool.pop(0)
        if self.options['max_reconnect_attempts'] > 0:
            if s.reconnects > self.options['max_reconnect_attempts']:
                continue
        self._server_pool.append(s)
        if s.last_attempt is not None and now < s.last_attempt + self.options[
            'reconnect_time_wait']:
            yield tornado.gen.sleep(self.options['reconnect_time_wait'])
        try:
            yield self._server_connect(s)
            self._current_server = s
            break
        except Exception as e:
            s.last_attempt = time.time()
            s.reconnects += 1
            self._err = e
            if self._error_cb is not None:
                self._error_cb(e)
            self._status = Client.RECONNECTING
            continue