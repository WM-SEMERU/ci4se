def drop_index_by_name(self, db_name, tbl_name, index_name, deleteData):
    self.send_drop_index_by_name(db_name, tbl_name, index_name, deleteData)
    return self.recv_drop_index_by_name()