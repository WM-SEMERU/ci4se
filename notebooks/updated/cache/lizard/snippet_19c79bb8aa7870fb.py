def create(self, file_or_path=None, data=None, obj_name=None, content_type=
    None, etag=None, content_encoding=None, content_length=None, ttl=None,
    chunked=False, metadata=None, chunk_size=None, headers=None,
    return_none=False):
    if (data, file_or_path) == (None, None):
        raise exc.NoContentSpecified(
            'You must specify either a file path, an open file-like object, or a stream of bytes when creating an object.'
            )
    src = data if data else file_or_path
    if src is file_or_path:
        obj_name = _validate_file_or_path(file_or_path, obj_name)
    if not obj_name:
        raise exc.MissingName(
            'No name for the object to be created has been specified, and none can be inferred from context'
            )
    if chunk_size:
        chunked = True
    if chunked:
        chunk_size = chunk_size or DEFAULT_CHUNKSIZE
    headers = headers or {}
    if metadata:
        metadata = _massage_metakeys(metadata, OBJECT_META_PREFIX)
        headers = metadata
    if ttl is not None:
        headers['X-Delete-After'] = ttl
    if src is data:
        self._upload(obj_name, data, content_type, content_encoding,
            content_length, etag, chunked, chunk_size, headers)
    elif hasattr(file_or_path, 'read'):
        self._upload(obj_name, file_or_path, content_type, content_encoding,
            content_length, etag, False, chunk_size, headers)
    else:
        with open(file_or_path, 'rb') as ff:
            self._upload(obj_name, ff, content_type, content_encoding,
                content_length, etag, False, chunk_size, headers)
    if return_none:
        return
    return self.get(obj_name)