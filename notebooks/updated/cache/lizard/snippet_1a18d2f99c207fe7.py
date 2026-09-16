def create(self, provider, names, **kwargs):
    mapper = salt.cloud.Map(self._opts_defaults())
    providers = self.opts['providers']
    if provider in providers:
        provider += ':{0}'.format(next(six.iterkeys(providers[provider])))
    else:
        return False
    if isinstance(names, six.string_types):
        names = names.split(',')
    ret = {}
    for name in names:
        vm_ = kwargs.copy()
        vm_['name'] = name
        vm_['driver'] = provider
        vm_['profile'] = None
        vm_['provider'] = provider
        ret[name] = salt.utils.data.simple_types_filter(mapper.create(vm_))
    return ret