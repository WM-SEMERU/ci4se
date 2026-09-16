def normalize(self):
    logger.debug('normalize: {}'.format(type(self).__name__))
    normalize_headers = self._normalize_headers()
    return TableData(self.__normalize_table_name(), normalize_headers, self
        ._normalize_rows(normalize_headers), dp_extractor=self._tabledata.
        dp_extractor, type_hints=self._type_hints)