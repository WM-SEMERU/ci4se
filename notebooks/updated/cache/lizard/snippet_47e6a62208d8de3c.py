def reconnect(self, exc=None):
    self.protocol = None
    if not self.closing:
        log.warning('disconnected from Rflink, reconnecting')
        self.loop.create_task(self.connect())