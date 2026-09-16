def upload_gallery_photo(self, gallery_id, source_amigo_id, file_obj,
    chunk_size=CHUNK_SIZE, force_chunked=False, metadata=None):
    simple_upload_url = 'related_tables/%s/upload' % gallery_id
    chunked_upload_url = 'related_tables/%s/chunked_upload' % gallery_id
    data = {'source_amigo_id': source_amigo_id}
    if isinstance(file_obj, basestring):
        data['filename'] = os.path.basename(file_obj)
    else:
        data['filename'] = os.path.basename(file_obj.name)
    if metadata:
        data.update(metadata)
    return self.upload_file(simple_upload_url, chunked_upload_url, file_obj,
        chunk_size=chunk_size, force_chunked=force_chunked, extra_data=data)