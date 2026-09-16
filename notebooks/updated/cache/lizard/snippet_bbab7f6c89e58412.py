def _children(self):
    for codeobj in self.parameters:
        yield codeobj
    for codeobj in self.body._children():
        yield codeobj