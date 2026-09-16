def close(self, name=None):
    tag = self._open_elements.pop()
    if name is not None and name != tag:
        raise Exception('Tag closing mismatch')
    self._pad()
    self._writer.endElement(_normalize_name(tag))
    self._newline()