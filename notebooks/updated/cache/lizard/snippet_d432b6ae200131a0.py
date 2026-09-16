def set_mode(self, *modes, **kwargs):
    if kwargs.get('private'):
        modes = [(mode << 5) for mode in modes]
        if mo.DECSCNM in modes:
            self.dirty.update(range(self.lines))
    self.mode.update(modes)
    if mo.DECCOLM in modes:
        self.saved_columns = self.columns
        self.resize(columns=132)
        self.erase_in_display(2)
        self.cursor_position()
    if mo.DECOM in modes:
        self.cursor_position()
    if mo.DECSCNM in modes:
        for line in self.buffer.values():
            line.default = self.default_char
            for x in line:
                line[x] = line[x]._replace(reverse=True)
        self.select_graphic_rendition(7)
    if mo.DECTCEM in modes:
        self.cursor.hidden = False