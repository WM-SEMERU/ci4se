def uncertaintyMap(self, psf, method='convolve', fitParams=None):
    img = scaleSignal(self.img, fitParams=fitParams)
    if method == 'convolve':
        blurred = convolve2d(img, psf, 'same')
        m = abs(img - blurred) / abs(img + blurred)
        m = np.nan_to_num(m)
        m *= self.std ** 2
        m[m > 1] = 1
        self.blur_distortion = m
        np.save('blurred', blurred)
        return m
    else:
        restored = unsupervised_wiener(img, psf)[0]
        m = abs(img - restored) / abs(img + restored)
        m = np.nan_to_num(m)
        m *= self.std ** 2
        m[m > 1] = 1
        self.blur_distortion = m
        return m, restored