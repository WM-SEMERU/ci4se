def restrictCatalogToObservableSpaceMMD(self, catalog):
    catalog.spatialBin(self.roi)
    sel_roi = catalog.pixel_roi_index >= 0
    sel_mag_1 = catalog.mag_1 < self.mask_1.mask_roi_sparse[catalog.
        pixel_roi_index]
    sel_mag_2 = catalog.mag_2 < self.mask_2.mask_roi_sparse[catalog.
        pixel_roi_index]
    sel_mmd = ugali.utils.binning.take2D(self.solid_angle_mmd, catalog.
        mag_2, catalog.mag_1, self.roi.bins_mag, self.roi.bins_mag) > 0.0
    sel = np.all([sel_roi, sel_mag_1, sel_mag_2, sel_mmd], axis=0)
    return sel