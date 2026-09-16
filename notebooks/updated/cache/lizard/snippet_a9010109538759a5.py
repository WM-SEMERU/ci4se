def read(self, entity=None, attrs=None, ignore=None, params=None):
    if attrs is None:
        attrs = self.read_json()
    attrs['from_'] = attrs.pop('from')
    if ignore is None:
        ignore = set()
    if attrs is not None and 'parameters' in attrs:
        attrs['subnet_parameters_attributes'] = attrs.pop('parameters')
    else:
        ignore.add('subnet_parameters_attributes')
    ignore.add('discovery')
    ignore.add('remote_execution_proxy')
    return super(Subnet, self).read(entity, attrs, ignore, params)