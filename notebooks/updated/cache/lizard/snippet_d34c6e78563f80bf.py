def _send_command(self, cmd=''):
    self.connection.write_channel(cmd + '\n')
    time.sleep(1)
    output = self.connection._read_channel_timing()
    output = self.connection.strip_ansi_escape_codes(output)
    output = self.connection.strip_backspaces(output)
    return output