def load(self, url, offset, length):
    headers = {}
    if offset != 0 or length != -1:
        headers['Range'] = BlockLoader._make_range_header(offset, length)
    if self.cookie_maker:
        if isinstance(self.cookie_maker, six.string_types):
            headers['Cookie'] = self.cookie_maker
        else:
            headers['Cookie'] = self.cookie_maker.make()
    if not self.session:
        self.session = requests.Session()
    r = self.session.get(url, headers=headers, stream=True)
    r.raise_for_status()
    return r.raw