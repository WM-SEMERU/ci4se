def sync_headers(cloud_obj, headers=None, header_patterns=HEADER_PATTERNS):
    if headers is None:
        headers = {}
    content_type = getattr(cloud_obj, 'content_type', None)
    if content_type == 'application/directory':
        return
    matched_headers = {}
    for pattern, pattern_headers in header_patterns:
        if pattern.match(cloud_obj.name):
            matched_headers.update(pattern_headers.copy())
    matched_headers.update(cloud_obj.headers)
    matched_headers.update(headers)
    if matched_headers != cloud_obj.headers:
        cloud_obj.headers = matched_headers
        cloud_obj.sync_metadata()