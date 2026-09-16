def put_file(self):
    destination = '{}/{}'.format(self.file_system, self.dest_file)
    self.scp_conn.scp_transfer_file(self.source_file, destination)
    self.scp_conn.close()