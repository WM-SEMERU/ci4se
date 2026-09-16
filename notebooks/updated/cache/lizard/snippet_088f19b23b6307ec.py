def get_con_id(self):
    con_id = ''
    if 'contribution' in self.tables:
        if 'id' in self.tables['contribution'].df.columns:
            con_id = str(self.tables['contribution'].df['id'].values[0])
    return con_id