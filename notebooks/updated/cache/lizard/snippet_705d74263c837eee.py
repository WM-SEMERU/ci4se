def add_section(self, section):
    if section.lower() == 'default':
        raise ValueError('Invalid section name: %s' % section)
    if section in self._sections:
        raise DuplicateSectionError(section)
    self._sections[section] = self._dict()