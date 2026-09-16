def get_table_fields(self, db_table):
    db_table_desc = self.introspection.get_table_description(self.cursor,
        db_table)
    return [t[0] for t in db_table_desc]