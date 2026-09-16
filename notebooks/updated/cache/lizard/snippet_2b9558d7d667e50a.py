def __upload_chunk(self, resource, chunk_size, bytes, bytes_start, bytes_read):
    headers = {'content-type': self.content_type, 'content-length': str(min
        ([chunk_size, self._file_size - bytes_read])), 'content-range':
        'bytes {0}-{1}/{2}'.format(bytes_start, bytes_read - 1, self.
        _file_size)}
    return Request(self._client, 'put', resource, domain=self.
        _DEFAULT_DOMAIN, headers=headers, body=bytes).perform()