def download(self, source, destination):
    self._handler.download(posix_path(source), destination)