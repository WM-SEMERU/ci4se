def message(self, level, *args):
    msg = ' '.join(str(o) for o in args)
    if level not in ('start', 'end', 'debug', 'info', 'warn', 'error'):
        return msg
    return '%s: %s' % (level, msg)