def compound(self):
    root = Compound()
    self._process(Nature.LBRACKET)
    while self.token.nature != Nature.RBRACKET:
        root.children.append(self.statement())
    self._process(Nature.RBRACKET)
    return root