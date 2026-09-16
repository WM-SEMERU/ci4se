def delete(Bucket, MFA=None, RequestPayer=None, Force=False, region=None,
    key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if Force:
            empty(Bucket, MFA=MFA, RequestPayer=RequestPayer, region=region,
                key=key, keyid=keyid, profile=profile)
        conn.delete_bucket(Bucket=Bucket)
        return {'deleted': True}
    except ClientError as e:
        return {'deleted': False, 'error': __utils__['boto3.get_error'](e)}