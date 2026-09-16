def explicit_rel_links(self, rels=('homepage', 'download')):
    for match in self._rel_re.finditer(self.content):
        found_rels = match.group(1).lower().split()
        for rel in rels:
            if rel in found_rels:
                break
        else:
            continue
        match = self._href_re.search(match.group(0))
        if not match:
            continue
        url = match.group(1) or match.group(2) or match.group(3)
        url = self.clean_link(urlparse.urljoin(self.base_url, url))
        yield Link(url, self)