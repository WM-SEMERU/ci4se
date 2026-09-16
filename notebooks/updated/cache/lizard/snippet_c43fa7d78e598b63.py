def get(self):
    r
    if not self._verify_auth():
        self.redirect('/login')
        return
    self.set_header('Content-Type', 'text/event-stream')
    self.set_header('Cache-Control', 'no-cache')
    self.set_header('Connection', 'keep-alive')
    self.write('retry: {0}\n'.format(400))
    self.flush()
    while True:
        try:
            event = yield self.application.event_listener.get_event(self)
            self.write('tag: {0}\n'.format(event.get('tag', '')))
            self.write(str('data: {0}\n\n').format(_json_dumps(event)))
            self.flush()
        except TimeoutException:
            break