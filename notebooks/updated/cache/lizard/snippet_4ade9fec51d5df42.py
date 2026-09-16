def connect_generators(self, debug=False):
    for mv_grid_district in self.mv_grid_districts():
        mv_grid_district.mv_grid.connect_generators(debug=debug)
        seed = int(cfg_ding0.get('random', 'seed'))
        random.seed(a=seed)
        for load_area in mv_grid_district.lv_load_areas():
            if not load_area.is_aggregated:
                for lv_grid_district in load_area.lv_grid_districts():
                    lv_grid_district.lv_grid.connect_generators(debug=debug)
                    if debug:
                        lv_grid_district.lv_grid.graph_draw(mode='LV')
            else:
                logger.info(
                    '{} is of type aggregated. LV generators are not connected to LV grids.'
                    .format(repr(load_area)))
    logger.info('=====> Generators connected')