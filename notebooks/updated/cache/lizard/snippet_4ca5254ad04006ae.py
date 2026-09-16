def title(self, value=None):
    if not value is None:
        if self.metadatatype == 'native':
            self.metadata['title'] = value
        else:
            self._title = value
    if self.metadatatype == 'native':
        if 'title' in self.metadata:
            return self.metadata['title']
        else:
            return None
    else:
        return self._title