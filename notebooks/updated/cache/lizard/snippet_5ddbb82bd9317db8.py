def _load(self, **kwargs):
    if self._check_existence_by_collection(self._meta_data['container'],
        kwargs['name']):
        return super(Rules, self)._load(**kwargs)
    msg = 'The rule named, {}, does not exist on the device.'.format(kwargs
        ['name'])
    raise NonExtantPolicyRule(msg)