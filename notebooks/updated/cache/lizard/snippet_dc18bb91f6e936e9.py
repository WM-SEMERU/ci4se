def str_with_sizes(self, max_name, max_remote_id, max_size):
    name_str = self.name.ljust(max_name)
    remote_id_str = self.remote_id.ljust(max_remote_id)
    size_str = self.size.ljust(max_size)
    return '{}    {}    {}    {}'.format(name_str, remote_id_str, size_str,
        self.file_hash)