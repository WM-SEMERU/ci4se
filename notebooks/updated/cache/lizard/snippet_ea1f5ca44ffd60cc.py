def fetch(self, max=None):
    if max:
        self.max = max
        n_pages = 0
        while not self._total_pages or n_pages < self._total_pages:
            self.fetch_next_page(True)
            n_pages += 1
        return self
    else:
        return self._fetch()