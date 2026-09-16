def set_branch_ids(self):
    ctr = 1
    for branch in self.graph_edges():
        branch['branch'].id_db = self.grid_district.id_db * 10 ** 4 + ctr
        ctr += 1
    for lv_load_area in self.grid_district.lv_load_areas():
        for lv_grid_district in lv_load_area.lv_grid_districts():
            ctr = 1
            for branch in lv_grid_district.lv_grid.graph_edges():
                branch['branch'].id_db = lv_grid_district.id_db * 10 ** 7 + ctr
                ctr += 1