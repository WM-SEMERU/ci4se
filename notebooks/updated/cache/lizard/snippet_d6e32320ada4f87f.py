def _WriteFileEntry(self, file_entry, data_stream_name, destination_file):
    source_file_object = file_entry.GetFileObject(data_stream_name=
        data_stream_name)
    if not source_file_object:
        return
    try:
        with open(destination_file, 'wb') as destination_file_object:
            source_file_object.seek(0, os.SEEK_SET)
            data = source_file_object.read(self._COPY_BUFFER_SIZE)
            while data:
                destination_file_object.write(data)
                data = source_file_object.read(self._COPY_BUFFER_SIZE)
    finally:
        source_file_object.close()