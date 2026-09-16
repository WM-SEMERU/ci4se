def set_branch_ids(self):
    for grid_district in self.mv_grid_districts():
        grid_district.mv_grid.set_branch_ids()
    logger.info('=====> Branch IDs set')