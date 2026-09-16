def register(self, slug, bundle, order=1, title=None):
    if slug in self._registry:
        raise AlreadyRegistered('The url %s is already registered' % slug)
    self._registry[slug] = bundle
    self._order[slug] = order
    if title:
        self._titles[slug] = title
    bundle.set_admin_site(self)