def send_pending_requests(self):
    assert_open(self)
    unsent_commands = self.commands
    if unsent_commands:
        self.commands = []
        if self.auto_batch:
            unsent_commands = auto_batch_commands(unsent_commands)
        buf = []
        for command_name, args, options, promise in unsent_commands:
            buf.append((command_name,) + tuple(args))
            self.pending_responses.append((command_name, options, promise))
        cmds = self.connection.pack_commands(buf)
        self._send_buf.extend(cmds)
    if not self._send_buf:
        return True
    self.send_buffer()
    return not self._send_buf