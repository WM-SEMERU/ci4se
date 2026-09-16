def Close(self):
    if not self._append:
        for field_name in self._fields:
            query = 'CREATE INDEX {0:s}_idx ON log2timeline ({0:s})'.format(
                field_name)
            self._cursor.execute(query)
            if self._set_status:
                self._set_status('Created index: {0:s}'.format(field_name))
    if self._set_status:
        self._set_status('Creating metadata...')
    for field in self._META_FIELDS:
        values = self._GetDistinctValues(field)
        self._cursor.execute('DELETE FROM l2t_{0:s}s'.format(field))
        for name, frequency in iter(values.items()):
            self._cursor.execute(
                'INSERT INTO l2t_{0:s}s ({0:s}s, frequency) VALUES("{1:s}", {2:d}) '
                .format(field, name, frequency))
    self._cursor.execute('DELETE FROM l2t_tags')
    for tag in self._ListTags():
        self._cursor.execute('INSERT INTO l2t_tags (tag) VALUES (?)', [tag])
    if self._set_status:
        self._set_status('Database created.')
    self._connection.commit()
    self._cursor.close()
    self._connection.close()
    self._cursor = None
    self._connection = None