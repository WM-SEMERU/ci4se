def streamReachAndWatershed(self, delineate, out_stream_order_grid,
    out_network_connectivity_tree, out_network_coordinates,
    out_stream_reach_file, out_watershed_grid, pit_filled_elevation_grid=
    None, flow_dir_grid=None, contributing_area_grid=None,
    stream_raster_grid=None, outlet_shapefile=None):
    log('PROCESS: StreamReachAndWatershed')
    if pit_filled_elevation_grid:
        self.pit_filled_elevation_grid = pit_filled_elevation_grid
    if flow_dir_grid:
        self.flow_dir_grid = flow_dir_grid
    if contributing_area_grid:
        self.contributing_area_grid = contributing_area_grid
    if stream_raster_grid:
        self.stream_raster_grid = stream_raster_grid
    cmd = [os.path.join(self.taudem_exe_path, 'streamnet'), '-fel', self.
        pit_filled_elevation_grid, '-p', self.flow_dir_grid, '-ad8', self.
        contributing_area_grid, '-src', self.stream_raster_grid, '-ord',
        out_stream_order_grid, '-tree', out_network_connectivity_tree,
        '-coord', out_network_coordinates, '-net', out_stream_reach_file,
        '-w', out_watershed_grid]
    if outlet_shapefile:
        cmd += ['-o', outlet_shapefile]
    if delineate:
        cmd += ['-sw']
    self._run_mpi_cmd(cmd)
    self._add_prj_file(self.pit_filled_elevation_grid, out_stream_order_grid)
    self._add_prj_file(self.pit_filled_elevation_grid, out_stream_reach_file)
    self._add_prj_file(self.pit_filled_elevation_grid, out_watershed_grid)