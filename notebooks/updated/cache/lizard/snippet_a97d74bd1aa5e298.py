def split(self):
    min_x, max_x, min_y, max_y = self.bounds
    mid_x, mid_y = (min_x + max_x) / 2, (min_y + max_y) / 2
    q1 = min_x, mid_x, mid_y, max_y
    q2 = min_x, mid_x, min_y, mid_y
    q3 = mid_x, max_x, mid_y, max_y
    q4 = mid_x, max_x, min_y, mid_y
    return [QuadTree(self.data, bounds=q1), QuadTree(self.data, bounds=q2),
        QuadTree(self.data, bounds=q3), QuadTree(self.data, bounds=q4)]