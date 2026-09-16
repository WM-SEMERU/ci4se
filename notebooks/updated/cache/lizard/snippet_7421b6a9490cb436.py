def set_primary_key(self, table, column):
    self.execute('ALTER TABLE {0} ADD PRIMARY KEY ({1})'.format(wrap(table),
        column))
    self._printer('\tAdded primary key to {0} on column {1}'.format(wrap(
        table), column))