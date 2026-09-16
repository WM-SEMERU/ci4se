def set_left_table(self, left_table=None):
    if left_table:
        self.left_table = TableFactory(table=left_table, owner=self.owner)
    else:
        self.left_table = self.get_left_table()