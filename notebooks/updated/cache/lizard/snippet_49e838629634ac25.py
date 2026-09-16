def set_cache_url(self):
    emails = ','.join(sorted(self.addresses))
    self.cache_url = '%s:%s' % (self.scheme, emails)