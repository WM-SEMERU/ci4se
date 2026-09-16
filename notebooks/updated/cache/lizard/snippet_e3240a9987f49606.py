def refresh_stats(self):
    self.tot_pix = 0
    self.tot_sea = 0
    self.tot_land = 0
    self.tot_blocked = 0
    for row in range(self.grd.grid_height):
        for col in range(self.grd.grid_width):
            self.tot_pix += 1
            val = self.grd.get_tile(row, col)
            if val == TERRAIN_SEA:
                self.tot_sea += 1
            elif val == TERRAIN_LAND:
                self.tot_land += 1
            else:
                self.tot_blocked += 1