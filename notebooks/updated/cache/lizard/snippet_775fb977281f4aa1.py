def find_bucket_keys(bucket_name, regex, region_name=None,
    aws_access_key_id=None, aws_secret_access_key=None):
    log = logging.getLogger(mod_logger + '.find_bucket_keys')
    matched_keys = []
    if not isinstance(regex, basestring):
        log.error('regex argument is not a string, found: {t}'.format(t=
            regex.__class__.__name__))
        return None
    if not isinstance(bucket_name, basestring):
        log.error('bucket_name argument is not a string, found: {t}'.format
            (t=bucket_name.__class__.__name__))
        return None
    s3resource = boto3.resource('s3', region_name=region_name,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=
        aws_secret_access_key)
    bucket = s3resource.Bucket(bucket_name)
    log.info('Looking up S3 keys based on regex: {r}'.format(r=regex))
    for item in bucket.objects.all():
        log.debug('Checking if regex matches key: {k}'.format(k=item.key))
        match = re.search(regex, item.key)
        if match:
            matched_keys.append(item.key)
    log.info('Found matching keys: {k}'.format(k=matched_keys))
    return matched_keys