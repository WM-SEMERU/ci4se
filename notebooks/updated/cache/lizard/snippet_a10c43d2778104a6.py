def output(self):
    return PostgresTarget(host=self.host, database=self.database, user=self
        .user, password=self.password, table=self.table, update_id=self.
        update_id, port=self.port)