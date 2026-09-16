def set_row_gap(self, value):
    value = str(value) + 'px'
    value = value.replace('pxpx', 'px')
    self.style['grid-row-gap'] = value