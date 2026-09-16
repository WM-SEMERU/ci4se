def _parseIsNonPairTag(self):
    self._isnonpairtag = False
    if self._iscomment:
        return
    if self._element.startswith('<') and self._element.endswith('/>'):
        self._isnonpairtag = True
    if self._istag and self._tagname.lower() in NONPAIR_TAGS:
        self._isnonpairtag = True