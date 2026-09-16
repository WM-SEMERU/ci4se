def set_elevation(self, elevation_grid_path, mask_shapefile):
    ele_file = ElevationGridFile(project_file=self.project_manager, session
        =self.db_session)
    ele_file.generateFromRaster(elevation_grid_path, mask_shapefile,
        load_raster_to_db=self.load_rasters_to_db)