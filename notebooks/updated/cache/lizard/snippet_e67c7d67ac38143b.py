def get_code(self):
    stub = []
    bases = '(' + ', '.join(self.bases) + ')' if len(self.bases) > 0 else ''
    slots = {'n': self.name, 'b': bases}
    if len(self.children) == 0 and len(self.variables) == 0:
        stub.append('class %(n)s%(b)s: ...' % slots)
    else:
        stub.append('class %(n)s%(b)s:' % slots)
        super_code = super().get_code() if PY3 else StubNode.get_code(self)
        for line in super_code:
            stub.append(INDENT + line)
    return stub