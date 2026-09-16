def _activate_URI(self, selfLinkuri):
    uri = urlparse.urlsplit(str(self._meta_data['bigip']._meta_data['uri']))
    attribute_reg = self._meta_data.get('attribute_registry', {})
    attrs = list(itervalues(attribute_reg))
    attrs = self._assign_stats(attrs)
    scheme, domain, path, qarg, frag = urlparse.urlsplit(selfLinkuri)
    path_uri = urlparse.urlunsplit((scheme, uri.netloc, path, '', ''))
    if not path_uri.endswith('/'):
        path_uri = path_uri + '/'
    qargs = urlparse.parse_qs(qarg)
    self._meta_data.update({'uri': path_uri, 'creation_uri_qargs': qargs,
        'creation_uri_frag': frag, 'allowed_lazy_attributes': attrs})