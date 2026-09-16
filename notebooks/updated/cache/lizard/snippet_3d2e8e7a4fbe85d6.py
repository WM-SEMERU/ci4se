def to_file(self, filepath=None):
    if filepath is None and self._filepath is None:
        raise TorrentError(
            'Unable to save torrent to file: no filepath supplied.')
    if filepath is not None:
        self._filepath = filepath
    with open(self._filepath, mode='wb') as f:
        f.write(self.to_string())