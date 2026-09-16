def read_cell(self, x, y):
    cell = self._sheet.row(x)[y]
    if self._file.xf_list[cell.xf_index].background.pattern_colour_index == 64:
        self._file.xf_list[cell.xf_index].background.pattern_colour_index = 9
    if self._file.xf_list[cell.xf_index
        ].background.pattern_colour_index in self.colors.keys():
        style = self.colors[self._file.xf_list[cell.xf_index].background.
            pattern_colour_index]
    else:
        style = self.xlwt.easyxf(
            'pattern: pattern solid; border: top thin, right thin, bottom thin, left thin;'
            )
        style.pattern.pattern_fore_colour = self._file.xf_list[cell.xf_index
            ].background.pattern_colour_index
        self.colors[self._file.xf_list[cell.xf_index].background.
            pattern_colour_index] = style
    style.font.name = self._file.font_list[self._file.xf_list[cell.xf_index
        ].font_index].name
    style.font.bold = self._file.font_list[self._file.xf_list[cell.xf_index
        ].font_index].bold
    if isinstance(self.header[y], tuple):
        header = self.header[y][0]
    else:
        header = self.header[y]
    if self.strip:
        if is_str_or_unicode(cell.value):
            cell.value = cell.value.strip()
    if self.style:
        return {header: (cell.value, style)}
    else:
        return {header: cell.value}