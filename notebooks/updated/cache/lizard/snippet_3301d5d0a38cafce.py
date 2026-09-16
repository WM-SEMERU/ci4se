def isempty(self, tables=None):
    tables = tables or self.tables
    for table in tables:
        if self.num_rows(table) > 0:
            return False
    return True