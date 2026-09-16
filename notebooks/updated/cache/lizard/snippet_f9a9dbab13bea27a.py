def _unify_values(self, section, vars):
    sectiondict = {}
    try:
        sectiondict = self._sections[section]
    except KeyError:
        if section != self.default_section:
            raise NoSectionError(section)
    vardict = {}
    if vars:
        for key, value in vars.items():
            if value is not None:
                value = str(value)
            vardict[self.optionxform(key)] = value
    return _ChainMap(vardict, sectiondict, self._defaults)