def _autodiscover(self):
    if not getattr(self, '_registerable_class', None):
        raise ImproperlyConfigured(
            'You must set a "_registerable_class" property in order to use autodiscovery.'
            )
    for mod_name in ('dashboard', 'panel'):
        for app in settings.INSTALLED_APPS:
            mod = import_module(app)
            try:
                before_import_registry = copy.copy(self._registry)
                import_module('%s.%s' % (app, mod_name))
            except Exception:
                self._registry = before_import_registry
                if module_has_submodule(mod, mod_name):
                    raise