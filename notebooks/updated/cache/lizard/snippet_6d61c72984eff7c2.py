def _check_success(self):
    cube_height = self.sim.data.body_xpos[self.cube_body_id][2]
    table_height = self.table_full_size[2]
    return cube_height > table_height + 0.1