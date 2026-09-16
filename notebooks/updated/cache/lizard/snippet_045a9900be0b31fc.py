def read_archive(self, header, prepend=None):
    _prefix = None
    _archive = False
    if header is not None:
        for kw in header.items():
            if kw[0][1:] in self.wcstrans.keys():
                _prefix = kw[0][0]
                _archive = True
                break
    if not _archive:
        self.archive(prepend=prepend)
        return
    if _prefix is not None:
        self.prepend = _prefix
    else:
        self.prepend = DEFAULT_PREFIX
    for key in self.wcstrans.keys():
        _archive_key = self._buildNewKeyname(key, _prefix)
        if key != 'pixel scale':
            if _archive_key in header:
                self.orig_wcs[_archive_key] = header[_archive_key]
            else:
                self.orig_wcs[_archive_key] = header[key]
            self.backup[key] = _archive_key
            self.revert[_archive_key] = key
    _cd11str = self.prepend + 'CD1_1'
    _cd21str = self.prepend + 'CD2_1'
    pscale = self.compute_pscale(self.orig_wcs[_cd11str], self.orig_wcs[
        _cd21str])
    _archive_key = self.prepend.lower() + 'pscale'
    self.orig_wcs[_archive_key] = pscale
    self.backup['pixel scale'] = _archive_key
    self.revert[_archive_key] = 'pixel scale'
    if 'WCSCDATE' in header:
        self.orig_wcs['WCSCDATE'] = header['WCSCDATE']
    else:
        self.orig_wcs['WCSCDATE'] = fileutil.getLTime()
    self.backup['WCSCDATE'] = 'WCSCDATE'
    self.revert['WCSCDATE'] = 'WCSCDATE'