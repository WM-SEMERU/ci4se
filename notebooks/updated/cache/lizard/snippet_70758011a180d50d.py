def reverse_url(self, datatype, url, verb='GET', urltype='single',
    api_version=None):
    api_version = api_version or 'v1'
    templates = getattr(self, 'URL_TEMPLATES__%s' % api_version)
    template_url = 'https://(?P<api_host>.+)/services/api/(?P<api_version>.+)'
    template_url += re.sub('{([^}]+)}', '(?P<\\1>.+)', templates[datatype][
        verb][urltype])
    m = re.match(template_url, url or '')
    if not m:
        raise KeyError("No reverse match from '%s' to %s.%s.%s" % (url,
            datatype, verb, urltype))
    r = m.groupdict()
    del r['api_host']
    if r.pop('api_version') != api_version:
        raise ValueError('API version mismatch')
    return r