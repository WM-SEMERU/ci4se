def clear_surroundings(self):
    cells_to_clear = self.grd.eight_neighbors(self.current_y, self.current_x)
    for cell in cells_to_clear:
        self.grd.set_tile(cell[0], cell[1], ' ')