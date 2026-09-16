def delayed_close(self):
    self.state = CLOSING
    self.server.io_loop.add_callback(self.close)