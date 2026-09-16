def _start_socket(self):
    if self._bm is None:
        self._bm = BinanceSocketManager(self._client)
    self._conn_key = self._bm.start_depth_socket(self._symbol, self.
        _depth_event)
    if not self._bm.is_alive():
        self._bm.start()
    while not len(self._depth_message_buffer):
        time.sleep(1)