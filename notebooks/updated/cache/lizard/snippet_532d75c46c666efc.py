def build_url(self):
    base_url, is_idn = url_norm(self.base_url, self.encoding)
    if self.base_ref:
        if ':' not in self.base_ref:
            self.base_ref = urljoin(self.parent_url, self.base_ref)
        self.url = urljoin(self.base_ref, base_url)
    elif self.parent_url:
        urlparts = list(urlparse.urlsplit(self.parent_url))
        urlparts[4] = ''
        parent_url = urlutil.urlunsplit(urlparts)
        self.url = urljoin(parent_url, base_url)
    else:
        self.url = base_url
    urlparts = list(urlparse.urlsplit(self.url))
    if urlparts[2]:
        urlparts[2] = urlutil.collapse_segments(urlparts[2])
    self.url = urlutil.urlunsplit(urlparts)
    self.urlparts = strformat.url_unicode_split(self.url)
    self.build_url_parts()
    self.url = urlutil.urlunsplit(self.urlparts)