def pass_bucket(f):

    @wraps(f)
    def decorate(*args, **kwargs):
        bucket_id = kwargs.pop('bucket_id')
        bucket = Bucket.get(as_uuid(bucket_id))
        if not bucket:
            abort(404, 'Bucket does not exist.')
        return f(*args, bucket=bucket, **kwargs)
    return decorate