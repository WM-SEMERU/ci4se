def _build_url(self):
    url_params = [BASE_URL, self.category + ' ratings', self.day, self.year,
        self.month]
    return SEARCH_URL.format(*url_params)