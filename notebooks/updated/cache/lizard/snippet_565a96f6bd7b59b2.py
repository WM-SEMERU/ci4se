def remove(self, filter=None):
    sql = build_delete(table_name=self.name, condition=filter)
    return self.cursor.execute(sql)