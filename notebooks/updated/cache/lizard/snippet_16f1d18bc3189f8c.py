def four_neighbors(self, row, col):
    ans = []
    if row > 0:
        ans.append((row - 1, col))
    if row < self.grid_height - 1:
        ans.append((row + 1, col))
    if col > 0:
        ans.append((row, col - 1))
    if col < self.grid_width - 1:
        ans.append((row, col + 1))
    return ans