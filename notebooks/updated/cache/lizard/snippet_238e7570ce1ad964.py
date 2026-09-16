def execute_sql(self, sql):
    cursor = self.get_cursor()
    cursor.execute(sql)
    return cursor