def copy2(src, dst, metadata=None, retry_params=None):
    common.validate_file_path(src)
    common.validate_file_path(dst)
    if metadata is None:
        metadata = {}
        copy_meta = 'COPY'
    else:
        copy_meta = 'REPLACE'
    metadata.update({'x-goog-copy-source': src, 'x-goog-metadata-directive':
        copy_meta})
    api = storage_api._get_storage_api(retry_params=retry_params)
    status, resp_headers, content = api.put_object(api_utils.
        _quote_filename(dst), headers=metadata)
    errors.check_status(status, [200], src, metadata, resp_headers, body=
        content)