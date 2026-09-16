def get_below_left_key_rect(self):
    key_left = self.row, self.col - 1, self.tab
    key_below_left = self.row + 1, self.col - 1, self.tab
    border_width_right = float(self.cell_attributes[key_below_left][
        'borderwidth_right']) / 2.0
    border_width_bottom = float(self.cell_attributes[key_left][
        'borderwidth_bottom']) / 2.0
    rect_below_left = (self.x - border_width_right, self.y - self.height,
        border_width_right, border_width_bottom)
    return key_below_left, rect_below_left