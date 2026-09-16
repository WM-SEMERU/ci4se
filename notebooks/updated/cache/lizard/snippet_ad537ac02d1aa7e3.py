def read_settings(self):
    extent = setting('user_extent', None, str)
    if extent:
        extent = QgsGeometry.fromWkt(extent)
        if not extent.isGeosValid():
            extent = None
    crs = setting('user_extent_crs', None, str)
    if crs:
        crs = QgsCoordinateReferenceSystem(crs)
        if not crs.isValid():
            crs = None
    mode = setting('analysis_extents_mode', HAZARD_EXPOSURE_VIEW)
    if crs and extent and mode == HAZARD_EXPOSURE_BOUNDINGBOX:
        self.extent.set_user_extent(extent, crs)
    self.extent.show_rubber_bands = setting('showRubberBands', False, bool)
    self.zoom_to_impact_flag = setting('setZoomToImpactFlag', True, bool)
    self.hide_exposure_flag = setting('setHideExposureFlag', False, bool)