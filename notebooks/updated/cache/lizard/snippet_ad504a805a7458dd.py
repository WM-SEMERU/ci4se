def _stream_blob(self, key, fileobj, progress_callback):
    file_size = None
    start_range = 0
    chunk_size = self.conn.MAX_CHUNK_GET_SIZE
    end_range = chunk_size - 1
    while True:
        try:
            blob = self.conn._get_blob(self.container_name, key,
                start_range=start_range, end_range=end_range)
            if file_size is None:
                file_size = self._parse_length_from_content_range(blob.
                    properties.content_range)
            fileobj.write(blob.content)
            start_range += blob.properties.content_length
            if start_range == file_size:
                break
            if blob.properties.content_length == 0:
                raise StorageError(
                    'Empty response received for {}, range {}-{}'.format(
                    key, start_range, end_range))
            end_range += blob.properties.content_length
            if end_range >= file_size:
                end_range = file_size - 1
            if progress_callback:
                progress_callback(start_range, file_size)
        except azure.common.AzureHttpError as ex:
            if ex.status_code == 416:
                return
            raise