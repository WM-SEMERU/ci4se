def copy_table_structure(self, source, destination, table):
    self.execute('CREATE TABLE {0}.{1} LIKE {2}.{1}'.format(destination,
        wrap(table), source))