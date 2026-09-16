def WriteEventBody(self, event):
    row = self._GetSanitizedEventValues(event)
    self._cursor.execute(self._INSERT_QUERY, row)
    self._count += 1
    if self._count % 10000 == 0:
        self._connection.commit()
        if self._set_status:
            self._set_status('Inserting event: {0:d}'.format(self._count))