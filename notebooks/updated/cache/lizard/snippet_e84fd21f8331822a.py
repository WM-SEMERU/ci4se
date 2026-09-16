def configure(self, *args, **kwargs):
    whitelist_keys_from_mappings = kwargs.get('whitelist_keys_from_mappings',
        False)
    whitelist = kwargs.get('whitelist')
    for item in args:
        if isinstance(item, string_types):
            _, ext = splitext(item)
            if ext == '.json':
                self._configure_from_json(item)
            elif ext in ('.cfg', '.py'):
                self._configure_from_pyfile(item)
            else:
                self._configure_from_module(item)
        elif isinstance(item, (types.ModuleType, type)):
            self._configure_from_object(item)
        elif hasattr(item, 'items'):
            self._configure_from_mapping(item, whitelist_keys=
                whitelist_keys_from_mappings, whitelist=whitelist)
        else:
            raise TypeError(
                'Could not determine a valid type for this configuration object: `{}`!'
                .format(item))
    self._run_post_configure_callbacks(args)