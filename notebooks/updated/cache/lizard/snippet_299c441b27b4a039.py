def stop_listener_thread(self):
    self.should_listen = False
    if self.sync_thread:
        self.sync_thread.kill()
        self.sync_thread.get()
    if self._handle_thread is not None:
        self._handle_thread.get()
    self.sync_thread = None
    self._handle_thread = None