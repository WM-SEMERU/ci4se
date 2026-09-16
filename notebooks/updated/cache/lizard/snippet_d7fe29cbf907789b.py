def _commit_hostname_handler(self, cmd):
    current_prompt = self.device.find_prompt().strip()
    terminating_char = current_prompt[-1]
    pattern = '[>#{}]\\s*$'.format(terminating_char)
    output = self.device.send_command_expect(cmd, expect_string=pattern)
    self.device.set_base_prompt()
    return output