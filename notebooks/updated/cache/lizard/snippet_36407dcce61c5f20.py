def delete(self, hdfs_path, recursive=False):
    return self.client.delete(hdfs_path, recursive=recursive)