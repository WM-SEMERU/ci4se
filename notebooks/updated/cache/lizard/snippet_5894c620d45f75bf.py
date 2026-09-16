def to_table_data(self):
    self._validate_source_data()
    header_list = []
    for json_record in self._buffer:
        for key in json_record:
            if key not in header_list:
                header_list.append(key)
    self._loader.inc_table_count()
    yield TableData(self._make_table_name(), header_list, self._buffer,
        dp_extractor=self._loader.dp_extractor, type_hints=self.
        _extract_type_hints(header_list))