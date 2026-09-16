def get(self, url=None, delimiter='/'):
    params = {'Delimiter': delimiter}
    bucket, obj_key = _parse_url(url)
    if bucket:
        params['Bucket'] = bucket
    else:
        return self.call('ListBuckets', response_data_key='Buckets')
    if obj_key:
        params['Prefix'] = obj_key
    objects = self.call('ListObjects', response_data_key='Contents', **params)
    if objects:
        for obj in objects:
            obj['url'] = 's3://{0}/{1}'.format(bucket, obj['Key'])
    return objects