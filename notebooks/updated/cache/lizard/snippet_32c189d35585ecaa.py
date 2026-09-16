def _process_depth_message(self, msg, buffer=False):
    if buffer and msg['u'] <= self._last_update_id:
        return
    elif msg['U'] != self._last_update_id + 1:
        self._init_cache()
    for bid in msg['b']:
        self._depth_cache.add_bid(bid)
    for ask in msg['a']:
        self._depth_cache.add_ask(ask)
    self._depth_cache.update_time = msg['E']
    if self._callback:
        self._callback(self._depth_cache)
    self._last_update_id = msg['u']
    if self._refresh_interval and int(time.time()) > self._refresh_time:
        self._init_cache()