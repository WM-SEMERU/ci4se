def micromanager_metadata(self):
    if not self.is_micromanager:
        return None
    result = read_micromanager_metadata(self._fh)
    result.update(self.pages[0].tags['MicroManagerMetadata'].value)
    return result