def render_table(self, headers, rows, style=None):
    table = self.table(headers, rows, style)
    table.render(self._io)