def set_scalebar_for_all(self, row_column_list=None, location='lower right'):
    if row_column_list is None:
        for subplot in self.subplots:
            subplot.set_scalebar(location)
    else:
        for row, column in row_column_list:
            subplot = self.get_subplot_at(row, column)
            subplot.set_scalebar(location)