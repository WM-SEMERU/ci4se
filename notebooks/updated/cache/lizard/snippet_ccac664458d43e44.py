def raw_diff(self):
    udiff_copy = self.copy_iterator()
    if self.__format == 'gitdiff':
        udiff_copy = self._parse_gitdiff(udiff_copy)
    return ''.join(udiff_copy)