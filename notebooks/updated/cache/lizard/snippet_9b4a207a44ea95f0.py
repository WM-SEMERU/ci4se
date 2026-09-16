def to_table_data(self):
    self._validate_source_data()
    self._loader.inc_table_count()
    yield TableData(self._make_table_name(), ['key', 'value'], [record for
        record in self._buffer.items()], dp_extractor=self._loader.
        dp_extractor, type_hints=self._extract_type_hints())