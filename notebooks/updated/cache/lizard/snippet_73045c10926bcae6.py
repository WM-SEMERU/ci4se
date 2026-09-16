def _docstring_key(self, line):
    decormatch = self.docparser.RE_DECOR.match(line)
    if decormatch is not None:
        key = '{}.{}'.format(self.docelement.name, decormatch.group('name'))
    else:
        key = self.element.name
    return key