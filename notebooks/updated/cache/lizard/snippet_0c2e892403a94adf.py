def _run_select(self):
    return self._connection.select(self.to_sql(), self.get_bindings(), not
        self._use_write_connection)