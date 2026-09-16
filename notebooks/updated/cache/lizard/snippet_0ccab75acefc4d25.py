def offsets(self):
    for path, tailedfile in self._tailedfiles.iteritems():
        yield path, tailedfile._offset