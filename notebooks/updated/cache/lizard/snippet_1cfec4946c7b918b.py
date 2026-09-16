def as_cache_key(self, ireq):
    name, version, extras = as_tuple(ireq)
    if not extras:
        extras_string = ''
    else:
        extras_string = '[{}]'.format(','.join(extras))
    return name, '{}{}'.format(version, extras_string)