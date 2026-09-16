def set_wsgi_params(self, module=None, callable_name=None, env_strategy=None):
    module = module or ''
    if '/' in module:
        self._set('wsgi-file', module, condition=module)
    else:
        self._set('wsgi', module, condition=module)
    self._set('callable', callable_name)
    self._set('wsgi-env-behaviour', env_strategy)
    return self._section