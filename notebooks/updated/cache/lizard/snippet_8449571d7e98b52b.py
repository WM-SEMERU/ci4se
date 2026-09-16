def create_bucket(self):
    bucket_exists = self._bucket_exists()
    if self.s3props.get('shared_bucket_target'):
        if bucket_exists:
            LOG.info('App uses shared bucket - %s ', self.bucket)
        else:
            LOG.error('Shared bucket %s does not exist', self.bucket)
            raise S3SharedBucketNotFound
    else:
        if self.region == 'us-east-1':
            _response = self.s3client.create_bucket(ACL=self.s3props[
                'bucket_acl'], Bucket=self.bucket)
        elif not bucket_exists:
            _response = self.s3client.create_bucket(ACL=self.s3props[
                'bucket_acl'], Bucket=self.bucket,
                CreateBucketConfiguration={'LocationConstraint': self.region})
        else:
            _response = (
                'bucket already exists, skipping create for non-standard region buckets.'
                )
        LOG.debug('Response creating bucket: %s', _response)
        LOG.info('%s - S3 Bucket Upserted', self.bucket)
        self._put_bucket_policy()
        self._put_bucket_website()
        self._put_bucket_logging()
        self._put_bucket_lifecycle()
        self._put_bucket_versioning()
        self._put_bucket_encryption()
        self._put_bucket_tagging()