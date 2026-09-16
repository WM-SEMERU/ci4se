def _get_or_create_s3_bucket(s3, name):
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket=name)
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False
        else:
            raise
    if not exists:
        s3.create_bucket(Bucket=name)
    return s3.Bucket(name)