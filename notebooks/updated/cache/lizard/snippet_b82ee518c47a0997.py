def parse_command(self, command):
    words = shlex.split(command.lower())
    return words[0], words[1:]