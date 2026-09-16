def create(Bucket, ACL=None, LocationConstraint=None, GrantFullControl=None,
    GrantRead=None, GrantReadACP=None, GrantWrite=None, GrantWriteACP=None,
    region=None, key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        kwargs = {}
        for arg in ('ACL', 'GrantFullControl', 'GrantRead', 'GrantReadACP',
            'GrantWrite', 'GrantWriteACP'):
            if locals()[arg] is not None:
                kwargs[arg] = str(locals()[arg])
        if LocationConstraint:
            kwargs['CreateBucketConfiguration'] = {'LocationConstraint':
                LocationConstraint}
        location = conn.create_bucket(Bucket=Bucket, **kwargs)
        conn.get_waiter('bucket_exists').wait(Bucket=Bucket)
        if location:
            log.info('The newly created bucket name is located at %s',
                location['Location'])
            return {'created': True, 'name': Bucket, 'Location': location[
                'Location']}
        else:
            log.warning('Bucket was not created')
            return {'created': False}
    except ClientError as e:
        return {'created': False, 'error': __utils__['boto3.get_error'](e)}