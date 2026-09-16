def deconstruct(self):
    name, path, args, kwargs = super(FKToVersion, self).deconstruct()
    if not kwargs['to'].endswith('_version'):
        kwargs['to'] = '{0}_version'.format(kwargs['to'])
    return name, path, args, kwargs