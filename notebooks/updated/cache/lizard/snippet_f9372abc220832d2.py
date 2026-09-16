def set_ylimits(self, row, column, min=None, max=None):
    subplot = self.get_subplot_at(row, column)
    subplot.set_ylimits(min, max)