def pattern(self):
    if not self._pattern:
        if self.operation in ['query', 'getmore', 'update', 'remove'
            ] or self.command in ['count', 'findandmodify']:
            self._pattern = self._find_pattern('query: ')
        elif self.command == 'find':
            self._pattern = self._find_pattern('filter: ')
    return self._pattern