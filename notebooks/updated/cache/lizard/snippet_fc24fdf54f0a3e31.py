def links(self):

    def clean(url):
        """Tidy up an URL."""
        scheme, netloc, path, params, query, frag = urlparse(url)
        return urlunparse((scheme, netloc, quote(path), params, query, frag))
    result = set()
    for match in self._href.finditer(self.data):
        d = match.groupdict('')
        rel = d['rel1'] or d['rel2'] or d['rel3'] or d['rel4'] or d['rel5'
            ] or d['rel6']
        url = d['url1'] or d['url2'] or d['url3']
        url = urljoin(self.base_url, url)
        url = unescape(url)
        url = self._clean_re.sub(lambda m: '%%%2x' % ord(m.group(0)), url)
        result.add((url, rel))
    result = sorted(result, key=lambda t: t[0], reverse=True)
    return result