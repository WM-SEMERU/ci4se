def delete(self, table, identifier):
    with self.locked() as conn:
        return conn.delete(table, identifier)