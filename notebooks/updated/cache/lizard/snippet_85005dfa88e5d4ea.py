def index_changed_aggregation_layer_combo(self, index):
    if index == 0:
        self.aggregation = None
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
    else:
        self.extent.clear_user_analysis_extent()
        self.aggregation = layer_from_combo(self.aggregation_layer_combo)
    self.validate_impact_function()