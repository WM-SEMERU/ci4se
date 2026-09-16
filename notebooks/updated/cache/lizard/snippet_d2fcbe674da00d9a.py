def clear(self):
    self._xroot = ElementTree.Element('settings')
    self._xroot.set('version', '1.0')
    self._xstack = [self._xroot]