def alias(self):
    if self._alias is None:
        if self.name in self.aliases_fix:
            self._alias = self.aliases_fix[self.name]
        else:
            self._alias = self.name.lower().replace(' ', '-').replace('(', ''
                ).replace(')', '')
    return self._alias