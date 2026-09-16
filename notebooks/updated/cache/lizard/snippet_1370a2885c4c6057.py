def dump(cls, message):
    if cls.verbose > 2:
        msg = '[DUMP] %s' % message
        cls.echo(msg)