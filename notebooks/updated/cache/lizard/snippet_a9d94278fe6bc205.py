def parse(self):
    try:
        if not os.path.getsize(self.ns.pathname):
            self.job.LOG.warn("Ignoring 0-byte metafile '%s'" % (self.ns.
                pathname,))
            return
        self.metadata = metafile.checked_open(self.ns.pathname)
    except EnvironmentError as exc:
        self.job.LOG.error("Can't read metafile '%s' (%s)" % (self.ns.
            pathname, str(exc).replace(": '%s'" % self.ns.pathname, '')))
        return
    except ValueError as exc:
        self.job.LOG.error("Invalid metafile '%s': %s" % (self.ns.pathname,
            exc))
        return
    self.ns.info_hash = metafile.info_hash(self.metadata)
    self.ns.info_name = self.metadata['info']['name']
    self.job.LOG.info("Loaded '%s' from metafile '%s'" % (self.ns.info_name,
        self.ns.pathname))
    try:
        name = self.job.proxy.d.name(self.ns.info_hash, fail_silently=True)
    except xmlrpc.HashNotFound:
        pass
    except xmlrpc.ERRORS as exc:
        if exc.faultString != 'Could not find info-hash.':
            self.job.LOG.error('While checking for #%s: %s' % (self.ns.
                info_hash, exc))
            return
    else:
        self.job.LOG.warn("Item #%s '%s' already added to client" % (self.
            ns.info_hash, name))
        return
    return True