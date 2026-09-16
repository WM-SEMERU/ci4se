def _endGenresNode(self, name, content):
    if name == 'class':
        self._genre = content
    elif name == 'relevance':
        self._relevance = content
    elif name == 'genre':
        if not self._error:
            self._importer.new_genre(self._programId, self._genre, self.
                _relevance)