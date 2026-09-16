def do_aprint(self, statement):
    self.poutput('aprint was called with argument: {!r}'.format(statement))
    self.poutput('statement.raw = {!r}'.format(statement.raw))
    self.poutput('statement.argv = {!r}'.format(statement.argv))
    self.poutput('statement.command = {!r}'.format(statement.command))