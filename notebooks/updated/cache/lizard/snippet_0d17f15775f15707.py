def pretty_str(self, indent=0):
    if self.parenthesis:
        return '{}({})'.format(' ' * indent, pretty_str(self.value))
    return pretty_str(self.value, indent=indent)