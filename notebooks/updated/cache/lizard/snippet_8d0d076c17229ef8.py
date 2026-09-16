def add_argument(self, parser, set_default=False):
    default = self.default if set_default else None
    kwargs = dict(nargs=self.nargs, default=default, help='%s [%s]' % (self
        .short, default))
    kwargs.update(self.extra)
    if self.flags:
        args = tuple(self.flags)
        kwargs.update({'dest': self.name, 'action': self.action or 'store'})
        if kwargs['action'] != 'store':
            kwargs.pop('type', None)
            kwargs.pop('nargs', None)
    elif self.nargs and self.name:
        args = self.name,
        kwargs.update({'metavar': self.meta or None})
    else:
        return
    if self.meta:
        kwargs['metavar'] = self.meta
    parser.add_argument(*args, **kwargs)