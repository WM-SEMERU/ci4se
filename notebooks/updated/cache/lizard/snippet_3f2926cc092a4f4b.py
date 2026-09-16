def create_json_archive(self):
    archive_data = {'packets': self.recv_msgs, 'dataset': self.dataset_name,
        'num_packets': len(self.recv_msgs), 'created': rnow()}
    self.write_to_file(archive_data, self.archive_file)