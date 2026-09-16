def _save_reference(self, filename):
    url = _make_internal_url(filename)
    with cython_context():
        self.__proxy__.save_reference(url)