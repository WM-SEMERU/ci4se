def pretty_print(self, indent=0):
    s = tab = ' ' * indent
    s += '%s: ' % self.tag
    if isinstance(self.value, basestring):
        s += self.value
    else:
        s += '\n'
        for e in self.value:
            s += e.pretty_print(indent + 4)
    s += '\n'
    return s