def pretty_str(self, indent=0):
    spaces = ' ' * indent
    params = ', '.join(map(lambda p: p.result + ' ' + p.name, self.parameters))
    if self.is_constructor:
        pretty = '{}{}({}):\n'.format(spaces, self.name, params)
    else:
        pretty = '{}{} {}({}):\n'.format(spaces, self.result, self.name, params
            )
    if self._definition is not self:
        pretty += spaces + '  [declaration]'
    else:
        pretty += self.body.pretty_str(indent + 2)
    return pretty