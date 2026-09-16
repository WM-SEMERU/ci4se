def blocking(self):
    return self.execute(sql.BLOCKING.format(query_column=self.query_column,
        pid_column=self.pid_column))