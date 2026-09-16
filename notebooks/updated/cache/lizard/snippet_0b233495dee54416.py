def set_wtscl(self, chip, wtscl_par):
    sci_chip = self._image[self.scienceExt, chip]
    exptime = 1
    _parval = 'unity'
    if wtscl_par is not None:
        if type(wtscl_par) == type(''):
            if not wtscl_par.isdigit():
                _wtscl_float = None
                try:
                    _wtscl_float = float(wtscl_par)
                except ValueError:
                    _wtscl_float = None
                if _wtscl_float is not None:
                    _wtscl = _wtscl_float
                elif wtscl_par == 'expsq':
                    _wtscl = exptime * exptime
                    _parval = 'expsq'
                else:
                    _wtscl = exptime
            else:
                _wtscl = float(wtscl_par)
        else:
            _wtscl = float(wtscl_par)
    else:
        _wtscl = exptime
    sci_chip._wtscl_par = _parval
    sci_chip._wtscl = _wtscl