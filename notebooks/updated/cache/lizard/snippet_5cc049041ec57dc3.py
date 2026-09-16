def get_l(self):
    cell_left = CellBorders(self.cell_attributes, *self.cell.
        get_left_key_rect())
    return cell_left.get_r()