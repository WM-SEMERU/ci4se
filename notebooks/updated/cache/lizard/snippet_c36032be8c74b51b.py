def cells_changed(self):
    self.total_size = sum(cell.size for cell in self.own_cells)
    self.total_mass = sum(cell.mass for cell in self.own_cells)
    self.scale = pow(min(1.0, 64.0 / self.total_size), 0.4
        ) if self.total_size > 0 else 1.0
    if self.own_ids:
        left = min(cell.pos.x for cell in self.own_cells)
        right = max(cell.pos.x for cell in self.own_cells)
        top = min(cell.pos.y for cell in self.own_cells)
        bottom = max(cell.pos.y for cell in self.own_cells)
        self.center = Vec(left + right, top + bottom) / 2