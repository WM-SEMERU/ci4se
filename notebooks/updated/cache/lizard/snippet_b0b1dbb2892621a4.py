def filter(self, source_file, encoding):
    with codecs.open(source_file, 'r', encoding=encoding) as f:
        text = f.read()
    return [filters.SourceText(self._filter(text), source_file, encoding,
        'context')]