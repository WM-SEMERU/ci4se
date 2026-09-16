def copy_part_from_key(self, src_bucket_name, src_key_name, part_num, start
    =None, end=None):
    if part_num < 1:
        raise ValueError('Part numbers must be greater than zero')
    query_args = 'uploadId=%s&partNumber=%d' % (self.id, part_num)
    if start is not None and end is not None:
        rng = 'bytes=%s-%s' % (start, end)
        provider = self.bucket.connection.provider
        headers = {provider.copy_source_range_header: rng}
    else:
        headers = None
    return self.bucket.copy_key(self.key_name, src_bucket_name,
        src_key_name, storage_class=None, headers=headers, query_args=
        query_args)