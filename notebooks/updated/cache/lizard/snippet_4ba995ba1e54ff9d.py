def get(self, test_id):
    self.select('*', 'test_id=?', [test_id])
    row = self._cursor.fetchone()
    if not row:
        raise KeyError('No report with test id %s in the DB' % test_id)
    values = self.row_to_dict(row)
    content = self._deserialize_dict(values['content'])
    return Report.from_dict(content)