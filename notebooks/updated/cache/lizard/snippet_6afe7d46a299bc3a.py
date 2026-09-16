def background_model(self, ignore_black=True, use_hsv=False, scale=8):
    data = self.data
    if use_hsv:
        pil_im = PImage.fromarray(self._data)
        pil_im = pil_im.convert('HSV')
        data = np.asarray(pil_im)
    nonblack_pixels = np.where(np.sum(self.data, axis=2) > 0)
    r_data = self.r_data
    g_data = self.g_data
    b_data = self.b_data
    if ignore_black:
        r_data = r_data[nonblack_pixels[0], nonblack_pixels[1]]
        g_data = g_data[nonblack_pixels[0], nonblack_pixels[1]]
        b_data = b_data[nonblack_pixels[0], nonblack_pixels[1]]
    bounds = 0, np.iinfo(np.uint8).max + 1
    num_bins = bounds[1] / scale
    r_hist, _ = np.histogram(r_data, bins=num_bins, range=bounds)
    g_hist, _ = np.histogram(g_data, bins=num_bins, range=bounds)
    b_hist, _ = np.histogram(b_data, bins=num_bins, range=bounds)
    hists = r_hist, g_hist, b_hist
    modes = [(0) for i in range(self.channels)]
    for i in range(self.channels):
        modes[i] = scale * np.argmax(hists[i])
    return modes