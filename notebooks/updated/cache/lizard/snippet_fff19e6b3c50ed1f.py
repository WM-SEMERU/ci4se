def create_resumable_upload_session(self, content_type=None, size=None,
    origin=None, client=None):
    extra_headers = {}
    if origin is not None:
        extra_headers['Origin'] = origin
    try:
        dummy_stream = BytesIO(b'')
        upload, _ = self._initiate_resumable_upload(client, dummy_stream,
            content_type, size, None, predefined_acl=None, extra_headers=
            extra_headers, chunk_size=self._CHUNK_SIZE_MULTIPLE)
        return upload.resumable_url
    except resumable_media.InvalidResponse as exc:
        _raise_from_invalid_response(exc)