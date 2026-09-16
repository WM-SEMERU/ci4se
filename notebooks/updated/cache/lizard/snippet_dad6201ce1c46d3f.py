def merge(self, across=False):
    url = self.build_url(self._endpoints.get('merge_range'))
    return bool(self.session.post(url, data={'across': across}))