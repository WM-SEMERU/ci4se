def insert_get_id(self, values, sequence=None):
    values = OrderedDict(sorted(values.items()))
    sql = self._grammar.compile_insert_get_id(self, values, sequence)
    values = self._clean_bindings(values.values())
    return self._processor.process_insert_get_id(self, sql, values, sequence)