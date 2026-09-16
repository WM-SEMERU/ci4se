def set_mask_from_shapefile(self, shapefile_path, cell_size):
    shapefile_path = os.path.abspath(shapefile_path)
    with tmp_chdir(self.project_directory):
        mask_name = '{0}.msk'.format(self.project_manager.name)
        msk_file = WatershedMaskFile(project_file=self.project_manager,
            session=self.db_session)
        msk_file.generateFromWatershedShapefile(shapefile_path, cell_size=
            cell_size, out_raster_path=mask_name, load_raster_to_db=self.
            load_rasters_to_db)