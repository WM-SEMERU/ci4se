def get_table_column_statistics(self, db_name, tbl_name, col_name):
    self.send_get_table_column_statistics(db_name, tbl_name, col_name)
    return self.recv_get_table_column_statistics()