def fmt_border(self, dimensions, t='m', border_style='utf8.a',
    border_formating={}):
    cells = []
    for column in dimensions:
        cells.append(self.bchar('h', t, border_style) * (dimensions[column] +
            2))
    border = '{}{}{}'.format(self.bchar('l', t, border_style), self.bchar(
        'm', t, border_style).join(cells), self.bchar('r', t, border_style))
    return self.fmt_text(border, **border_formating)