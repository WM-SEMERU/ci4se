def construct_command(self, command, keys=None, opts=None):
    cstr = [command]
    if keys:
        for key in keys:
            if isinstance(keys[key], list):
                ncstr = []
                for nest in keys[key]:
                    ncstr.append('%s=%s' % (key, self._escape_str(nest)))
                cstr.append('|'.join(ncstr))
            else:
                cstr.append('%s=%s' % (key, self._escape_str(keys[key])))
    if opts:
        for opt in opts:
            cstr.append('-%s' % opt)
    return ' '.join(cstr)