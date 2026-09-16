def variable_declaration(self):
    self._process(Nature.LET)
    node = VariableDeclaration(assignment=self.assignment())
    self._process(Nature.SEMI)
    return node