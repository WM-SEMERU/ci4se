def get_urls(self):
    base_urls = super(SimpleRouter, self).get_urls()
    single_urls = sum([r.urls for r in self._single_object_registry], [])
    nested_urls = sum([r.urls for r in self._nested_object_registry], [])
    return base_urls + single_urls + nested_urls