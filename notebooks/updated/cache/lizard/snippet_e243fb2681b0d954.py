def _call(self, x):
    if self.impl == 'pywt':
        coeffs = pywt.wavedecn(x, wavelet=self.pywt_wavelet, level=self.
            nlevels, mode=self.pywt_pad_mode, axes=self.axes)
        return pywt.ravel_coeffs(coeffs, axes=self.axes)[0]
    else:
        raise RuntimeError("bad `impl` '{}'".format(self.impl))