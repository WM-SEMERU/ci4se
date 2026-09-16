def auto_fit_columns(self):
    url = self.build_url(self._endpoints.get('auto_fit_columns'))
    return bool(self.session.post(url))