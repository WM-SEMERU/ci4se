def pretty_str(self, indent=0):
    spaces = ' ' * indent
    pretty = '{}namespace {}:\n'.format(spaces, self.name)
    pretty += '\n\n'.join(c.pretty_str(indent + 2) for c in self.children)
    return pretty