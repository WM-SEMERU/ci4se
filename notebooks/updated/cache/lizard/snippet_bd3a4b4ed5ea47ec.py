def find_table(self, search):
    tables = []
    for table in self.tables:
        if glob.fnmatch.fnmatch(table.name, search):
            tables.append(table)
    return TableSet(tables)