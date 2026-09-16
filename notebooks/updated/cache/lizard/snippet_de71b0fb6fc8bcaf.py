def binary(self):

    def _get_binary():
        parser = self._create_directory_parser(self.path)
        if not parser.entries:
            raise errors.NotFoundError('No entries found', self.path)
        pattern = re.compile(self.binary_regex, re.IGNORECASE)
        for entry in parser.entries:
            try:
                self._binary = pattern.match(entry).group()
                break
            except Exception:
                continue
        else:
            raise errors.NotFoundError('Binary not found in folder', self.path)
    self._retry_check_404(_get_binary)
    return self._binary