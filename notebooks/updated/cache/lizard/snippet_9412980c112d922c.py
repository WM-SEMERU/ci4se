def returns_fake(self, *args, **kwargs):
    exp = self._get_current_call()
    endpoint = kwargs.get('name', exp.call_name)
    name = self._endpoint_name(endpoint)
    kwargs['name'] = '%s()' % name
    fake = self.__class__(*args, **kwargs)
    exp.return_val = fake
    return fake