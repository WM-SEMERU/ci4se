def _parseCounters(self, data):
    info_dict = util.NestedDict()
    for line in data.splitlines():
        mobj = re.match('^\\s*([\\w\\.]+)\\s*=\\s*(\\S.*)$', line)
        if mobj:
            key, value = mobj.groups()
            klist = key.split('.')
            info_dict.set_nested(klist, parse_value(value))
    return info_dict