def typing(self, *, channel: str):
    payload = {'id': self._next_msg_id(), 'type': 'typing', 'channel': channel}
    self.send_over_websocket(payload=payload)