def _match_type(self, i):
    self.col_match = self.RE_TYPE.match(self._source[i])
    if self.col_match is not None:
        self.section = 'types'
        self.el_type = CustomType
        self.el_name = self.col_match.group('name')
        return True
    else:
        return False