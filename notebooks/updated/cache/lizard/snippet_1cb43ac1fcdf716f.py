def run_powerflow(self, session, method='onthefly', export_pypsa=False,
    debug=False):
    if method == 'db':
        pypsa_io.delete_powerflow_tables(session)
        for grid_district in self.mv_grid_districts():
            if export_pypsa:
                export_pypsa_dir = repr(grid_district.mv_grid)
            else:
                export_pypsa_dir = None
            grid_district.mv_grid.run_powerflow(session, method='db',
                export_pypsa_dir=export_pypsa_dir, debug=debug)
    elif method == 'onthefly':
        for grid_district in self.mv_grid_districts():
            if export_pypsa:
                export_pypsa_dir = repr(grid_district.mv_grid)
            else:
                export_pypsa_dir = None
            grid_district.mv_grid.run_powerflow(session, method='onthefly',
                export_pypsa_dir=export_pypsa_dir, debug=debug)