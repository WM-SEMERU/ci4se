def is_available(self, fname):
    self._assert_file_in_registry(fname)
    source = self.get_url(fname)
    response = requests.head(source, allow_redirects=True)
    return bool(response.status_code == 200)