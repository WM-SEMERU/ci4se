def get_num_partitions_by_filter(self, db_name, tbl_name, filter):
    self.send_get_num_partitions_by_filter(db_name, tbl_name, filter)
    return self.recv_get_num_partitions_by_filter()