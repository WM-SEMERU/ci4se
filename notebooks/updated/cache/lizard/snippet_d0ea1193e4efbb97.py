def get_file_to_bytes(self, share_name, directory_name, file_name,
    start_range=None, end_range=None, range_get_content_md5=None,
    progress_callback=None, max_connections=1, max_retries=5, retry_wait=
    1.0, timeout=None):
    _validate_not_none('share_name', share_name)
    _validate_not_none('file_name', file_name)
    stream = BytesIO()
    file = self.get_file_to_stream(share_name, directory_name, file_name,
        stream, start_range, end_range, range_get_content_md5,
        progress_callback, max_connections, max_retries, retry_wait, timeout)
    file.content = stream.getvalue()
    return file