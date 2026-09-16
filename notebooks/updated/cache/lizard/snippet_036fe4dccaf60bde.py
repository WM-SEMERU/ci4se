def put_cors(Bucket, CORSRules, region=None, key=None, keyid=None, profile=None
    ):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if CORSRules is not None and isinstance(CORSRules, six.string_types):
            CORSRules = salt.utils.json.loads(CORSRules)
        conn.put_bucket_cors(Bucket=Bucket, CORSConfiguration={'CORSRules':
            CORSRules})
        return {'updated': True, 'name': Bucket}
    except ClientError as e:
        return {'updated': False, 'error': __utils__['boto3.get_error'](e)}