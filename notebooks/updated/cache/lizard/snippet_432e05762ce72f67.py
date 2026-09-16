def dump(self, output, close_after_write=True):
    self.open(output)
    try:
        self.make_worksheet(self.table_name)
        self.write_table()
    finally:
        if close_after_write:
            self.close()