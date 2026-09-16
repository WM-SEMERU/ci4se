def get_all(self, qry, tpl):
    self.cur.execute(qry, tpl)
    result = self.cur.fetchall()
    return result