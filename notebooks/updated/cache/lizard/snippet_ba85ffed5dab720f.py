def setInstrumentParameters(self, instrpars):
    pri_header = self._image[0].header
    if self._isNotValid(instrpars['gain'], instrpars['gnkeyword']):
        instrpars['gnkeyword'] = 'ATODGAIN'
    if self._isNotValid(instrpars['rdnoise'], instrpars['rnkeyword']):
        instrpars['rnkeyword'] = 'READNSE'
    if self._isNotValid(instrpars['exptime'], instrpars['expkeyword']):
        instrpars['expkeyword'] = 'EXPTIME'
    for chip in self.returnAllChips(extname=self.scienceExt):
        chip._gain = self.getInstrParameter(instrpars['gain'], pri_header,
            instrpars['gnkeyword'])
        chip._rdnoise = self.getInstrParameter(instrpars['rdnoise'],
            pri_header, instrpars['rnkeyword'])
        chip._exptime = self.getInstrParameter(instrpars['exptime'], chip.
            header, instrpars['expkeyword'])
        if (chip._gain is None or chip._rdnoise is None or chip._exptime is
            None):
            print('ERROR: invalid instrument task parameter')
            raise ValueError
        chip._effGain = chip._gain
        self._assignSignature(chip._chip)
    self.doUnitConversions()