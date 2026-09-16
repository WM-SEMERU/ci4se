def indication(self, *args, **kwargs):
    if not self.current_terminal:
        raise RuntimeError('no active terminal')
    if not isinstance(self.current_terminal, Server):
        raise RuntimeError('current terminal not a server')
    self.current_terminal.indication(*args, **kwargs)