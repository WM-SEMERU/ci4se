def as_file(self):
    use_data_if_no_file = not self._file and self._data
    if use_data_if_no_file:
        if self._base64_file_content:
            if isinstance(self._data, str):
                content = self._data.encode()
            else:
                content = self._data
            self._file = _create_temp_file_with_content(base64.
                standard_b64decode(content))
        else:
            self._file = _create_temp_file_with_content(self._data)
    if self._file and not os.path.isfile(self._file):
        raise ConfigException('File does not exists: %s' % self._file)
    return self._file