def _link(self, *args, **kwargs):
    if self._record.redirect_url:
        return links.resolve(self._record.redirect_url, self.search_path,
            kwargs.get('absolute'))
    return self._permalink(*args, **kwargs)