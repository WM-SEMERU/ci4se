def from_tabledata(self, value, is_overwrite_table_name=True):
    super(ExcelTableWriter, self).from_tabledata(value)
    if self.is_opened():
        self.make_worksheet(self.table_name)