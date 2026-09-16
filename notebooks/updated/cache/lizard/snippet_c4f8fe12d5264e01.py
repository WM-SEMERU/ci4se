def add_row(self, text, link=None, bold=False, align=None):
    if not self.table_columns_left:
        self.write('<tr>')
        self.table_columns_left = self.table_columns
    self.write('<td')
    if align:
        self.write(' style="text-align:{}"', align)
    self.write('>')
    if bold:
        self.write('<b>')
    if link:
        self.write('<a href="{}">', self._rel(link))
    self.write(text)
    if link:
        self.write('</a>')
    if bold:
        self.write('</b>')
    self.write('</td>')
    self.table_columns_left -= 1
    if not self.table_columns_left:
        self.write('</tr>')