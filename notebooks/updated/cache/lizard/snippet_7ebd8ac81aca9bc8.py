def list_objects(self, bucket_name, prefix='', recursive=False):
    is_valid_bucket_name(bucket_name)
    if prefix is None:
        prefix = ''
    method = 'GET'
    query = {'max-keys': '1000', 'prefix': prefix}
    if not recursive:
        query['delimiter'] = '/'
    marker = ''
    is_truncated = True
    while is_truncated:
        if marker:
            query['marker'] = marker
        headers = {}
        response = self._url_open(method, bucket_name=bucket_name, query=
            query, headers=headers)
        objects, is_truncated, marker = parse_list_objects(response.data,
            bucket_name=bucket_name)
        for obj in objects:
            yield obj