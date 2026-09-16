def _ctx_get_or_create(self, key, creation_function, context, **kw):
    if not self.template.cache_enabled:
        return creation_function()
    return self.impl.get_or_create(key, creation_function, **self.
        _get_cache_kw(kw, context))