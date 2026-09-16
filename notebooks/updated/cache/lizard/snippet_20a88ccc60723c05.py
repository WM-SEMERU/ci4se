def addMember(self, imagePtr=None):
    numchips = imagePtr._numchips
    log.info('Computing static mask:\n')
    chips = imagePtr.group
    if chips is None:
        chips = imagePtr.getExtensions()
    for chip in chips:
        chipid = imagePtr.scienceExt + ',' + str(chip)
        chipimage = imagePtr.getData(chipid)
        signature = imagePtr[chipid].signature
        if signature not in self.masklist or len(self.masklist) == 0:
            self.masklist[signature] = self._buildMaskArray(signature)
            maskname = constructFilename(signature)
            self.masknames[signature] = maskname
        else:
            chip_sig = buildSignatureKey(signature)
            for s in self.masknames:
                if chip_sig in self.masknames[s]:
                    maskname = self.masknames[s]
                    break
        imagePtr[chipid].outputNames['staticMask'] = maskname
        stats = ImageStats(chipimage, nclip=3, fields='mode')
        mode = stats.mode
        rms = stats.stddev
        nbins = len(stats.histogram)
        del stats
        log.info('  mode = %9f;   rms = %7f;   static_sig = %0.2f' % (mode,
            rms, self.static_sig))
        if nbins >= 2:
            sky_rms_diff = mode - self.static_sig * rms
            np.bitwise_and(self.masklist[signature], np.logical_not(np.less
                (chipimage, sky_rms_diff)), self.masklist[signature])
        del chipimage