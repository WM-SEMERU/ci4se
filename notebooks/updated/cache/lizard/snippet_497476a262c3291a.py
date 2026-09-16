def add_highlight(self, field, fragment_size=None, number_of_fragments=None,
    fragment_offset=None, type=None):
    if self._highlight is None:
        self._highlight = HighLighter('<b>', '</b>')
    self._highlight.add_field(field, fragment_size, number_of_fragments,
        fragment_offset, type=type)
    return self