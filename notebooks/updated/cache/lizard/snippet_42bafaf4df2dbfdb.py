def get_value(self, section, option, default=None):
    ret = default
    try:
        ret = self.parser.get(section, option)
    except NoOptionError:
        pass
    if ret is not None:
        try:
            match = self.re_pattern.findall(ret)
            for m in match:
                ret = ret.replace(m, system_exec(m[1:-1]))
        except TypeError:
            pass
    return ret