def is_valid_bucket_name(bucket_name):
    if len(bucket_name) < 3:
        raise InvalidBucketError(
            'Bucket name cannot be less than 3 characters.')
    if len(bucket_name) > 63:
        raise InvalidBucketError(
            'Bucket name cannot be more than 63 characters.')
    if '..' in bucket_name:
        raise InvalidBucketError('Bucket name cannot have successive periods.')
    match = _VALID_BUCKETNAME_REGEX.match(bucket_name)
    if match is None or match.end() != len(bucket_name):
        raise InvalidBucketError(
            'Bucket name does not follow S3 standards. Bucket: {0}'.format(
            bucket_name))
    return True