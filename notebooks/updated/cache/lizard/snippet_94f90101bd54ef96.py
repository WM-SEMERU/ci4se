def _execute_backend_on_spec(self):
    api_no_aliases_cache = None
    for attr_key in dir(self.backend_module):
        attr_value = getattr(self.backend_module, attr_key)
        if inspect.isclass(attr_value) and issubclass(attr_value, Backend
            ) and not inspect.isabstract(attr_value):
            self._logger.info('Running backend: %s', attr_value.__name__)
            backend = attr_value(self.build_path, self.backend_args)
            if backend.preserve_aliases:
                api = self.api
            else:
                if not api_no_aliases_cache:
                    api_no_aliases_cache = remove_aliases_from_api(self.api)
                api = api_no_aliases_cache
            try:
                backend.generate(api)
            except Exception:
                raise BackendException(attr_value.__name__, traceback.
                    format_exc()[:-1])