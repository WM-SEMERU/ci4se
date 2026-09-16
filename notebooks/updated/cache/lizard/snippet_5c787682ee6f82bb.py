def _append_hdu_info(self, ext):
    hdu_type = self._FITS.movabs_hdu(ext + 1)
    if hdu_type == IMAGE_HDU:
        hdu = ImageHDU(self._FITS, ext, **self.keys)
    elif hdu_type == BINARY_TBL:
        hdu = TableHDU(self._FITS, ext, **self.keys)
    elif hdu_type == ASCII_TBL:
        hdu = AsciiTableHDU(self._FITS, ext, **self.keys)
    else:
        mess = 'extension %s is of unknown type %s this is probably a bug'
        mess = mess % (ext, hdu_type)
        raise IOError(mess)
    self.hdu_list.append(hdu)
    self.hdu_map[ext] = hdu
    extname = hdu.get_extname()
    if not self.case_sensitive:
        extname = extname.lower()
    if extname != '':
        if extname not in self.hdu_map:
            self.hdu_map[extname] = hdu
        ver = hdu.get_extver()
        if ver > 0:
            key = '%s-%s' % (extname, ver)
            self.hdu_map[key] = hdu