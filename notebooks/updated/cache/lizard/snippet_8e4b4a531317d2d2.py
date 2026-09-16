def execute(self, statement, parameters=None):
    self._check_closed()
    if not parameters:
        self._execute_direct(statement)
    else:
        self.executemany(statement, parameters=[parameters])
    return self