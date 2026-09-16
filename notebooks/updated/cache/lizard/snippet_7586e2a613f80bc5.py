def _fake_openenumerateinstances(self, namespace, **params):
    self._validate_namespace(namespace)
    self._validate_open_params(**params)
    result_t = self._fake_enumerateinstances(namespace, **params)
    return self._open_response(result_t[0][2], namespace,
        'PullInstancesWithPath', **params)