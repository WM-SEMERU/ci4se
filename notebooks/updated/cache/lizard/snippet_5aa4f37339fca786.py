def copy_object(self, source_bucket, source_object_name, dest_bucket=None,
    dest_object_name=None, metadata={}, amz_headers={}):
    dest_bucket = dest_bucket or source_bucket
    dest_object_name = dest_object_name or source_object_name
    amz_headers['copy-source'] = '/%s/%s' % (source_bucket, source_object_name)
    details = self._details(method=b'PUT', url_context=self._url_context(
        bucket=dest_bucket, object_name=dest_object_name), metadata=
        metadata, amz_headers=amz_headers)
    d = self._submit(self._query_factory(details))
    return d