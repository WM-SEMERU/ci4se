def open(self, name_or_info, mode='r', pwd=None):
    ef = super(VerifyingZipFile, self).open(name_or_info, mode, pwd)
    if isinstance(name_or_info, zipfile.ZipInfo):
        name = name_or_info.filename
    else:
        name = name_or_info
    if name in self._expected_hashes and self._expected_hashes[name
        ] is not None:
        expected_hash = self._expected_hashes[name]
        try:
            _update_crc_orig = ef._update_crc
        except AttributeError:
            warnings.warn(
                'Need ZipExtFile._update_crc to implement file hash verification (in Python >= 2.7)'
                )
            return ef
        running_hash = self._hash_algorithm()
        if hasattr(ef, '_eof'):

            def _update_crc(data):
                _update_crc_orig(data)
                running_hash.update(data)
                if ef._eof and running_hash.digest() != expected_hash:
                    raise BadWheelFile('Bad hash for file %r' % ef.name)
        else:

            def _update_crc(data, eof=None):
                _update_crc_orig(data, eof=eof)
                running_hash.update(data)
                if eof and running_hash.digest() != expected_hash:
                    raise BadWheelFile('Bad hash for file %r' % ef.name)
        ef._update_crc = _update_crc
    elif self.strict and name not in self._expected_hashes:
        raise BadWheelFile('No expected hash for file %r' % ef.name)
    return ef