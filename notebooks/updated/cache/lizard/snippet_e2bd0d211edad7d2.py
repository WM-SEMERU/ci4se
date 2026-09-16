def canonical_key(self, key):
    if key.startswith('/'):
        return urlparse.urljoin(self.base_uri, key)
    else:
        return self.curies.expand(key)