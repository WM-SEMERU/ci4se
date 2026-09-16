def get_mean_width(self):
    assert 1 not in self.lons.shape, 'mean width is only defined for mesh of more than one row and more than one column of points'
    _, cell_length, cell_width, cell_area = self.get_cell_dimensions()
    widths = numpy.sum(cell_width, axis=0)
    column_areas = numpy.sum(cell_area, axis=0)
    mean_cell_lengths = numpy.sum(cell_length * cell_area, axis=0
        ) / column_areas
    return numpy.sum(widths * mean_cell_lengths) / numpy.sum(mean_cell_lengths)