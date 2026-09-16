def selection_range(self):
    selected = self.selectionModel().selection()
    if self.selection_is_empty:
        return -1, -1, -1, -1

    def range_to_tuple(rng):
        return rng.row(), rng.column()
    top_left = min(range_to_tuple(rng.topLeft()) for rng in selected)
    bottom_right = max(range_to_tuple(rng.bottomRight()) for rng in selected)
    return top_left[0], bottom_right[0], top_left[1], bottom_right[1] + 1