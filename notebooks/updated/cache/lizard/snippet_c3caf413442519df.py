def get_column_def(self):
    static = 'static' if self.static else ''
    db_type = self.db_type.format(self.value_type.db_type)
    return '{} {} {}'.format(self.cql, db_type, static)