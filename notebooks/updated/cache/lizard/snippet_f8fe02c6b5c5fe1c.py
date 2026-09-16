def cmdloop(self):
    while True:
        cmdline = input(self.prompt)
        tokens = shlex.split(cmdline)
        if not tokens:
            if self.last_cmd:
                tokens = self.last_cmd
            else:
                print('No previous command.')
                continue
        if tokens[0] not in self.commands:
            print('Invalid command')
            continue
        command = self.commands[tokens[0]]
        self.last_cmd = tokens
        try:
            if command(self.state, tokens):
                break
        except CmdExit:
            continue
        except Exception as e:
            if e not in self.safe_exceptions:
                logger.exception('Error!')