def disconnect(self, receiver=None, sender=None, dispatch_uid=None):
    if dispatch_uid:
        lookup_key = dispatch_uid, _make_id(sender)
    else:
        lookup_key = _make_id(receiver), _make_id(sender)
    disconnected = False
    with self.lock:
        self._clear_dead_receivers()
        for index in range(len(self.receivers)):
            r_key, _ = self.receivers[index]
            if r_key == lookup_key:
                disconnected = True
                del self.receivers[index]
                break
        self.sender_receivers_cache.clear()
    return disconnected