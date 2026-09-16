def get_preflist(self, bucket, key):
    if not self.preflists():
        raise NotImplementedError('fetching preflists is not supported.')
    bucket_type = self._get_bucket_type(bucket.bucket_type)
    url = self.preflist_path(bucket.name, key, bucket_type=bucket_type)
    status, headers, body = self._request('GET', url)
    if status == 200:
        preflist = json.loads(bytes_to_str(body))
        return preflist['preflist']
    else:
        raise RiakError('Error getting bucket/key preflist.')