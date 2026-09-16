def scan(self, filetypes=None):
    self.logger.debug('Scanning FS content.')
    checksums = self.filetype_filter(self._filesystem.checksums('/'),
        filetypes=filetypes)
    self.logger.debug('Querying %d objects to VTotal.', len(checksums))
    for files in chunks(checksums, size=self.batchsize):
        files = dict(reversed(e) for e in files)
        response = vtquery(self._apikey, files.keys())
        yield from self.parse_response(files, response)