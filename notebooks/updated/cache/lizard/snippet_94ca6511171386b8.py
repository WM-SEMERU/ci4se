def avg(self, field):
    q = Query(self.connection).from_table(self, fields=[AvgField(field)])
    rows = q.select(bypass_safe_limit=True)
    return list(rows[0].values())[0]