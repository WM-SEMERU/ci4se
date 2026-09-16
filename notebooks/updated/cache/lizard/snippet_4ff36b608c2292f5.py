def _init_class_from_url(self):
    from bugzilla import RHBugzilla
    if isinstance(self, RHBugzilla):
        return
    c = None
    if 'bugzilla.redhat.com' in self.url:
        log.info('Using RHBugzilla for URL containing bugzilla.redhat.com')
        c = RHBugzilla
    else:
        try:
            extensions = self._proxy.Bugzilla.extensions()
            if 'RedHat' in extensions.get('extensions', {}):
                log.info('Found RedHat bugzilla extension, using RHBugzilla')
                c = RHBugzilla
        except Fault:
            log.debug('Failed to fetch bugzilla extensions', exc_info=True)
    if not c:
        return
    self.__class__ = c