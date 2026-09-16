def get_option(self, name, section=None, vars=None, expect=None):
    vars = vars if vars else self.default_vars
    if section is None:
        section = self.default_section
    opts = self.get_options(section, opt_keys=[name], vars=vars)
    if opts:
        return opts[name]
    elif self._narrow_expect(expect):
        raise ValueError("no option '{}' found in section {}".format(name,
            section))