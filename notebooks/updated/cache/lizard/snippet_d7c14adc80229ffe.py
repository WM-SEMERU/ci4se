def _format_value(self, val):
    name = self.name + ':'
    if not self.multiline or '\n' not in val:
        val = '{0} {1}'.format(name.ljust(self._text_prefix_len), val)
    else:
        spacer = '\n' + ' ' * (self._text_prefix_len + 1)
        val = '{0}{1}{2}'.format(name, spacer, spacer.join(val.split('\n')))
    return val