def _pruneCMD(self, minimum_solid_angle):
    logger.info('Pruning mask based on minimum solid angle of %.2f deg^2' %
        minimum_solid_angle)
    self.solid_angle_cmd *= self.solid_angle_cmd > minimum_solid_angle
    if self.solid_angle_cmd.sum() == 0:
        msg = 'Pruned mask contains no solid angle.'
        logger.error(msg)
        raise Exception(msg)
    index_mag, index_color = np.nonzero(self.solid_angle_cmd)
    mag = self.roi.centers_mag[index_mag]
    color = self.roi.centers_color[index_color]
    if self.config.params['catalog']['band_1_detection']:
        mag_1 = mag
        mag_2 = mag_1 - color
        self.mag_1_clip = np.max(mag_1) + 0.5 * self.roi.delta_mag
        self.mag_2_clip = np.max(mag_2) + 0.5 * self.roi.delta_color
    else:
        mag_2 = mag
        mag_1 = color + mag_2
        self.mag_1_clip = np.max(mag_1) + 0.5 * self.roi.delta_color
        self.mag_2_clip = np.max(mag_2) + 0.5 * self.roi.delta_mag
    logger.info('Clipping mask 1 at %.2f mag' % self.mag_1_clip)
    logger.info('Clipping mask 2 at %.2f mag' % self.mag_2_clip)
    self.mask_1.mask_roi_sparse = np.clip(self.mask_1.mask_roi_sparse, 0.0,
        self.mag_1_clip)
    self.mask_2.mask_roi_sparse = np.clip(self.mask_2.mask_roi_sparse, 0.0,
        self.mag_2_clip)