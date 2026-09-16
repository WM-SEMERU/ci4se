def pprint(self, stream=None, indent=1, width=80, depth=None):
    pp.pprint(to_literal(self), stream, indent, width, depth)