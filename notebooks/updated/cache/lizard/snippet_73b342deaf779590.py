def create_file_from_stream(self, share_name, directory_name, file_name,
    stream, count, content_settings=None, metadata=None, progress_callback=
    None, max_connections=1, max_retries=5, retry_wait=1.0, timeout=None):
    _validate_not_none('share_name', share_name)
    _validate_not_none('file_name', file_name)
    _validate_not_none('stream', stream)
    _validate_not_none('count', count)
    if count < 0:
        raise TypeError(_ERROR_VALUE_NEGATIVE.format('count'))
    self.create_file(share_name, directory_name, file_name, count,
        content_settings, metadata, timeout)
    _upload_file_chunks(self, share_name, directory_name, file_name, count,
        self.MAX_RANGE_SIZE, stream, max_connections, max_retries,
        retry_wait, progress_callback, timeout)