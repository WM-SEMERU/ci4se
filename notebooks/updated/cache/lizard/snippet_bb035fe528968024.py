def chunk(self, count):
    for chunk in self._connection.select_many(count, self.to_sql(), self.
        get_bindings(), not self._use_write_connection):
        yield chunk