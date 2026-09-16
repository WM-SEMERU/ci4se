def to_s3_uri(code_dict):
    try:
        uri = 's3://{bucket}/{key}'.format(bucket=code_dict['S3Bucket'],
            key=code_dict['S3Key'])
        version = code_dict.get('S3ObjectVersion', None)
    except (TypeError, AttributeError):
        raise TypeError('Code location should be a dictionary')
    if version:
        uri += '?versionId=' + version
    return uri