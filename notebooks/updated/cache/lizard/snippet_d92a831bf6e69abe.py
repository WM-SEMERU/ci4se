def buildDiscoveryURL(self):
    if self.wildcard:
        assert self.host.startswith('.'), self.host
        www_domain = 'www' + self.host
        return '%s://%s%s' % (self.proto, www_domain, self.path)
    else:
        return self.unparsed