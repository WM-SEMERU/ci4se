def upsert(self, table, value, update_columns=None, commit=True):
    if not isinstance(value, dict):
        raise TypeError('Input value should be a dictionary')
    if not update_columns:
        update_columns = value.keys()
    value_q, _args = self._value_parser(value, columnname=False)
    _sql = ''.join(['INSERT INTO ', self._backtick(table), ' (', self.
        _backtick_columns(value), ') VALUES ', '(', value_q, ') ',
        'ON DUPLICATE KEY UPDATE ', ', '.join(['='.join([k, 'VALUES(' + k +
        ')']) for k in update_columns]), ';'])
    if self.debug:
        return self.cur.mogrify(_sql, _args)
    self.cur.execute(_sql, _args)
    if commit:
        self.conn.commit()
    return self.cur.lastrowid