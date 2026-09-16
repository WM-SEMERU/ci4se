def get_above_key_rect(self):
    key_above = self.row - 1, self.col, self.tab
    border_width_bottom = float(self.cell_attributes[key_above][
        'borderwidth_bottom']) / 2.0
    rect_above = (self.x, self.y - border_width_bottom, self.width,
        border_width_bottom)
    return key_above, rect_above