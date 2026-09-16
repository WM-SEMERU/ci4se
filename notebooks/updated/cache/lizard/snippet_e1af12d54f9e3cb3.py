def get_option_int(self, name, section=None, vars=None, expect=None):
    val = self.get_option(name, section, vars, expect)
    if val:
        return int(val)