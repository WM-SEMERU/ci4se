def restoreWCS(self, prepend=None):
    image = self.rootname
    if prepend:
        _prepend = prepend
    elif self.prepend:
        _prepend = self.prepend
    else:
        _prepend = None
    fimg = fileutil.openImage(image, mode='update')
    _root, _iextn = fileutil.parseFilename(self.rootname)
    _extn = fileutil.getExtn(fimg, _iextn)
    if len(self.backup) > 0:
        for newkey in self.revert.keys():
            if newkey != 'opscale':
                _orig_key = self.revert[newkey]
                _extn.header[_orig_key] = _extn.header[newkey]
    elif _prepend:
        for key in self.wcstrans.keys():
            if key != 'pixel scale':
                _okey = self._buildNewKeyname(key, _prepend)
                if _okey in _extn.header:
                    _extn.header[key] = _extn.header[_okey]
                else:
                    print('No original WCS values found. Exiting...')
                    break
    else:
        print('No original WCS values found. Exiting...')
    fimg.close()
    del fimg