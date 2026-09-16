def get_file_contents(self, file_key):
    self._raise_unimplemented_error()
    uri = '/'.join([self.api_uri, self.files_suffix, file_key, self.
        file_contents_suffix])
    return self._req('get', uri)