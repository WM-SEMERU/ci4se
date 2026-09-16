def quit(self):
    self._running = False
    self._quit = True
    self.ioloop.add_callback(self.ioloop.stop)
    if hasattr(self, 'xmlrpc_server'):
        self.xmlrpc_ioloop.add_callback(self.xmlrpc_server.stop)
        self.xmlrpc_ioloop.add_callback(self.xmlrpc_ioloop.stop)