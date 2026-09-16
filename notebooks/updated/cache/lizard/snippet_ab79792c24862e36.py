def get_settings(self, section=None, defaults=None):
    section = self._maybe_get_default_name(section)
    if self.filepath is None:
        return {}
    parser = self._get_parser(defaults)
    defaults = parser.defaults()
    try:
        raw_items = parser.items(section)
    except NoSectionError:
        return {}
    local_conf = OrderedDict()
    get_from_globals = {}
    for option, value in raw_items:
        if option.startswith('set '):
            name = option[4:].strip()
            defaults[name] = value
        elif option.startswith('get '):
            name = option[4:].strip()
            get_from_globals[name] = value
            local_conf[name] = None
        else:
            if option in defaults:
                continue
            local_conf[option] = value
    for option, global_option in get_from_globals.items():
        local_conf[option] = defaults[global_option]
    return ConfigDict(local_conf, defaults, self)