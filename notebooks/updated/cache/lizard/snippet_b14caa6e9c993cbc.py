def received_winch(self):

    def process_winch():
        if self._callbacks:
            self._callbacks.terminal_size_changed()
    self.call_from_executor(process_winch)