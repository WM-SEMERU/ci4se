def query_fetch_all(self, query, values):
    self.cursor.execute(query, values)
    retval = self.cursor.fetchall()
    self.__close_db()
    return retval