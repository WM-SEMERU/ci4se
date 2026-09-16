def upload_file(self, simple_upload_url, chunked_upload_url, file_obj,
    chunk_size=CHUNK_SIZE, force_chunked=False, extra_data=None):
    if isinstance(file_obj, string_types):
        file_obj = open(file_obj, 'rb')
        close_file = True
    else:
        close_file = False
    file_obj.seek(0, os.SEEK_END)
    file_size = file_obj.tell()
    file_obj.seek(0)
    try:
        if (simple_upload_url and not force_chunked and file_size <
            MAX_SIZE_SIMPLE_UPLOAD):
            return self.post(simple_upload_url, data=extra_data, files={
                'datafile': file_obj})
        data = {}
        md5_hash = hashlib.md5()
        start_byte = 0
        while True:
            chunk = file_obj.read(chunk_size)
            md5_hash.update(chunk)
            end_byte = start_byte + len(chunk) - 1
            content_range = 'bytes %d-%d/%d' % (start_byte, end_byte, file_size
                )
            ret = self.post(chunked_upload_url, data=data, files={
                'datafile': chunk}, headers={'Content-Range': content_range})
            data.setdefault('upload_id', ret['upload_id'])
            start_byte = end_byte + 1
            if start_byte == file_size:
                break
        if chunked_upload_url.endswith('/'):
            chunked_upload_complete_url = chunked_upload_url + 'complete'
        else:
            chunked_upload_complete_url = chunked_upload_url + '/complete'
        data['md5'] = md5_hash.hexdigest()
        if extra_data:
            data.update(extra_data)
        return self.post(chunked_upload_complete_url, data=data)
    finally:
        if close_file:
            file_obj.close()