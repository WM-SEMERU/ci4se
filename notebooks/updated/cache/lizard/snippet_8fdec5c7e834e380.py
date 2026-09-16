def as_sql(self, qn, connection=None):
    if self.bit:
        return '(%s.%s | %d)' % (qn(self.table_alias), qn(self.column),
            self.bit.mask), []
    return '(%s.%s & %d)' % (qn(self.table_alias), qn(self.column), self.
        bit.mask), []