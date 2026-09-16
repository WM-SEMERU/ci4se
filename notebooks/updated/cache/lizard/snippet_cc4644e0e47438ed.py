def RegisterMessageHandler(self, handler, lease_time, limit=1000):
    self.UnregisterMessageHandler()
    self.handler_stop = False
    self.handler_thread = threading.Thread(name='message_handler', target=
        self._MessageHandlerLoop, args=(handler, lease_time, limit))
    self.handler_thread.daemon = True
    self.handler_thread.start()