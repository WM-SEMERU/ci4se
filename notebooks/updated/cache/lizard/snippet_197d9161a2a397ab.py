def indent(self, indent_count):
    if indent_count < 1:
        return self
    s = [('\t' * indent_count + line) for line in self.splitlines(False)]
    s = '\n'.join(s)
    return type(self)(s)