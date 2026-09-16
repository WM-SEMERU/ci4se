def put_file(self, remote_path, local_source_file, **kwargs):
    if kwargs.get('chunked', True):
        return self._put_file_chunked(remote_path, local_source_file, **kwargs)
    stat_result = os.stat(local_source_file)
    headers = {}
    if kwargs.get('keep_mtime', True):
        headers['X-OC-MTIME'] = str(int(stat_result.st_mtime))
    if remote_path[-1] == '/':
        remote_path += os.path.basename(local_source_file)
    file_handle = open(local_source_file, 'rb', 8192)
    res = self._make_dav_request('PUT', remote_path, data=file_handle,
        headers=headers)
    file_handle.close()
    return res