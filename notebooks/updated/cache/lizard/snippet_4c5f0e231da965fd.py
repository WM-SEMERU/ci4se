def load_data(self, table_name, obj, database=None, **kwargs):
    _database = self.db_name
    self.set_database(database)
    self.con.load_table(table_name, obj, **kwargs)
    self.set_database(_database)