def build_mv_grid_district(self, poly_id, subst_id, grid_district_geo_data,
    station_geo_data):
    mv_station = MVStationDing0(id_db=subst_id, geo_data=station_geo_data)
    mv_grid = MVGridDing0(network=self, id_db=poly_id, station=mv_station)
    mv_grid_district = MVGridDistrictDing0(id_db=poly_id, mv_grid=mv_grid,
        geo_data=grid_district_geo_data)
    mv_grid.grid_district = mv_grid_district
    mv_station.grid = mv_grid
    self.add_mv_grid_district(mv_grid_district)
    return mv_grid_district