def prompt(self, message, text_input=False, timeout_s=None, cli_color=''):
    self.start_prompt(message, text_input, cli_color)
    return self.wait_for_prompt(timeout_s)