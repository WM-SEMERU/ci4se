def _make_absolute(self, link):
    parsed = urlparse(link)._asdict()
    if not parsed['netloc']:
        return urljoin(self.base_url, link)
    if not parsed['scheme']:
        parsed['scheme'] = urlparse(self.base_url).scheme
        parsed = (v for v in parsed.values())
        return urlunparse(parsed)
    return link