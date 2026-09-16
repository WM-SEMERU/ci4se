def head(self, n=6):
    q = self._query_templates['column']['head'].format(column=self.name,
        schema=self.schema, table=self.table, n=n)
    return pd.read_sql(q, self._con)[self.name]