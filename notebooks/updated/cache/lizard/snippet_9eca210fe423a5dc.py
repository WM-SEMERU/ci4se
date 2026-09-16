def _children(self):
    for codeobj in self.body._children():
        yield codeobj
    for catch_block in self.catches:
        for codeobj in catch_block._children():
            yield codeobj
    for codeobj in self.finally_body._children():
        yield codeobj