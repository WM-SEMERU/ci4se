def UnregisterMessageHandler(self, timeout=None):
    if self.handler_thread:
        self.handler_stop = True
        self.handler_thread.join(timeout)
        if self.handler_thread.isAlive():
            raise RuntimeError('Message handler thread did not join in time.')
        self.handler_thread = None