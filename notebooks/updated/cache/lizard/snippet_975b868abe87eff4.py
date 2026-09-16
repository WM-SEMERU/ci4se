def handler(self, reply):
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, self.
            display.display, None, None)
        if self.escape(event):
            self.stop()
        else:
            self._tap(event)