def set_table(self, table):
    super(MultiField, self).set_table(table)
    if self.field and self.field.table is None:
        self.field.set_table(self.table)