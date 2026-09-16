def print_unfinished_line(self):
    if self.state is STATE_RUNNING:
        if not callbacks.process(self.read_buffer):
            self.print_lines(self.read_buffer)
        self.read_buffer = b''