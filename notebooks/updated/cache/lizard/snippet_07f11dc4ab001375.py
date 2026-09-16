def _sanitize_output(self, output, strip_command=False, command_string=None,
    strip_prompt=False):
    if self.ansi_escape_codes:
        output = self.strip_ansi_escape_codes(output)
    output = self.normalize_linefeeds(output)
    if strip_command and command_string:
        command_string = self.normalize_linefeeds(command_string)
        output = self.strip_command(command_string, output)
    if strip_prompt:
        output = self.strip_prompt(output)
    return output