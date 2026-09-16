def set_mlimits(self, row, column, min=None, max=None):
    subplot = self.get_subplot_at(row, column)
    subplot.set_mlimits(min, max)