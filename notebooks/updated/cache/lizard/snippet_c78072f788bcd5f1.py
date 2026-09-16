def cmd_split(self, line):
    cmd, *args = line.lstrip().split(' ', 1)
    return self.root_command.subcommands[cmd], ' '.join(args)