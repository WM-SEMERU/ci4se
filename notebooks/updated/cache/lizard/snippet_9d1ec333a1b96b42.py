def get_partitions_pspec(self, db_name, tbl_name, max_parts):
    self.send_get_partitions_pspec(db_name, tbl_name, max_parts)
    return self.recv_get_partitions_pspec()