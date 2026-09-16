def get_input_kwargs(self, key=None, default=None):
    warnings.warn(
        '`get_input_kwargs` is deprecated; use `get_catalog_info` instead.',
        DeprecationWarning)
    return self.get_catalog_info(key, default)