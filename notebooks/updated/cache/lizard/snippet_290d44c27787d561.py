def column(self):
    for i in my_xrange(self._column_query_pos, self.pos):
        if self.text[i] == '\t':
            self._column += self.tab_size
            self._column -= self._column % self.tab_size
        else:
            self._column += 1
    self._column_query_pos = self.pos
    return self._column