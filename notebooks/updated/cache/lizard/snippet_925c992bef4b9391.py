def _parse(self):
    with open(self.filename, 'r') as fobj:
        lines = fobj.read().split('\n')
    self.header = MOPHeader(self.subfmt).parser(lines)
    self.data = MOPDataParser(self.header).parse(lines)