def add_table(self, rows, cols):
    width = self.width if self.width is not None else Inches(1)
    table = super(_Cell, self).add_table(rows, cols, width)
    self.add_paragraph()
    return table