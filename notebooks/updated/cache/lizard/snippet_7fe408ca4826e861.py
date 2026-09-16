def get_region(self, move_x, move_y):
    top_left = max(move_y - 1, 0), max(move_x - 1, 0)
    bottom_right = min(move_y + 1, self.board_height - 1), min(move_x + 1, 
        self.board_width - 1)
    region_sum = self.mine_map[top_left[0]:bottom_right[0] + 1, top_left[1]
        :bottom_right[1] + 1].sum()
    return top_left, bottom_right, region_sum