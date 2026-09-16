def y_max(self):
    end_y = max(y for y, *_ in self.iterator())
    if self.combined:
        end_y += self.group_offset
    return end_y + 2 * self.group_offset