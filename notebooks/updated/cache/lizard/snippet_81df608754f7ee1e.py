def delete_tagging(Bucket, region=None, key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        conn.delete_bucket_tagging(Bucket=Bucket)
        return {'deleted': True, 'name': Bucket}
    except ClientError as e:
        return {'deleted': False, 'error': __utils__['boto3.get_error'](e)}