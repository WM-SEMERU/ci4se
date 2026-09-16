def set_bucket_props(self, bucket, props):
    bucket_type = self._get_bucket_type(bucket.bucket_type)
    url = self.bucket_properties_path(bucket.name, bucket_type=bucket_type)
    headers = {'Content-Type': 'application/json'}
    content = json.dumps({'props': props})
    status, _, body = self._request('PUT', url, headers, content)
    if status == 401:
        raise SecurityError('Not authorized to set bucket properties.')
    elif status != 204:
        raise RiakError('Error setting bucket properties.')
    return True