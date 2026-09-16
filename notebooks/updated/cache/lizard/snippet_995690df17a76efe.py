def resolve_tv_show(self, title, year=None):
    r = self.search_tv_show(title)
    return self._match_results(r, title, year)