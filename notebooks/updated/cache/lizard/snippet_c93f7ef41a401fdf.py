def _put_bucket_policy(self):
    if self.s3props['bucket_policy']:
        policy_str = json.dumps(self.s3props['bucket_policy'])
        _response = self.s3client.put_bucket_policy(Bucket=self.bucket,
            Policy=policy_str)
    else:
        _response = self.s3client.delete_bucket_policy(Bucket=self.bucket)
    LOG.debug('Response adding bucket policy: %s', _response)
    LOG.info('S3 Bucket Policy Attached')