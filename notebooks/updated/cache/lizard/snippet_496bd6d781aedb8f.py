def _fake_openreferenceinstances(self, namespace, **params):
    self._validate_namespace(namespace)
    self._validate_open_params(**params)
    params['ObjectName'] = params['InstanceName']
    del params['InstanceName']
    result = self._fake_references(namespace, **params)
    objects = [] if result is None else [x[2] for x in result[0][2]]
    return self._open_response(objects, namespace, 'PullInstancesWithPath',
        **params)