def diagonals(self):
    left_top_shifts = map(lambda i: (-(i + 1), -(i + 1)), range(min(self.
        left_distance, self.top_distance)))
    left_bottom_shifts = map(lambda i: (-(i + 1), +(i + 1)), range(min(self
        .left_distance, self.bottom_distance)))
    right_top_shifts = map(lambda i: (+(i + 1), -(i + 1)), range(min(self.
        right_distance, self.top_distance)))
    right_bottom_shifts = map(lambda i: (+(i + 1), +(i + 1)), range(min(
        self.right_distance, self.bottom_distance)))
    return set(chain(left_top_shifts, left_bottom_shifts, right_top_shifts,
        right_bottom_shifts))