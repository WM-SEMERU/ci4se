def complete(self, text, state):
    result = cmd.Cmd.complete(self, text, state)
    if self.argparser_completer:
        self._make_argparser()
    return result