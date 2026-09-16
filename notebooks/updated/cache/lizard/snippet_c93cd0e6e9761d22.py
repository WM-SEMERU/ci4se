def make_url_absolute(self, url, resolve_base=False):
    if self.config['url']:
        if resolve_base:
            ubody = self.doc.unicode_body()
            base_url = find_base_url(ubody)
            if base_url:
                return urljoin(base_url, url)
        return urljoin(self.config['url'], url)
    else:
        return url