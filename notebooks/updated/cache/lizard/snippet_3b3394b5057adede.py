def _urls(self):
    urlpatterns = self._get_default_urlpatterns()
    self._autodiscover()
    for dash in self._registry.values():
        dash._autodiscover()
    self._load_panel_customization()
    if self._conf.get('customization_module', None):
        customization_module = self._conf['customization_module']
        bits = customization_module.split('.')
        mod_name = bits.pop()
        package = '.'.join(bits)
        mod = import_module(package)
        try:
            before_import_registry = copy.copy(self._registry)
            import_module('%s.%s' % (package, mod_name))
        except Exception:
            self._registry = before_import_registry
            if module_has_submodule(mod, mod_name):
                raise
    for dash in self._registry.values():
        urlpatterns.append(url('^%s/' % dash.slug, _wrapped_include(dash.
            _decorated_urls)))
    return urlpatterns, self.namespace, self.slug