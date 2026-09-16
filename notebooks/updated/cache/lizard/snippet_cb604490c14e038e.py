def windows_from_blocksize(self, blocksize_xy=512):
    meta = self._get_template_for_given_resolution(self.dst_res, 'meta')
    width = meta['width']
    height = meta['height']
    blocksize_wins = windows_from_blocksize(blocksize_xy, width, height)
    self.windows = np.array([win[1] for win in blocksize_wins])
    self.windows_row = np.array([win[0][0] for win in blocksize_wins])
    self.windows_col = np.array([win[0][1] for win in blocksize_wins])
    return self