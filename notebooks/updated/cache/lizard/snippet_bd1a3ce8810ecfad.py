def _require_bucket(self, bucket_name):
    if not self.exists(bucket_name) and not self.claim_bucket(bucket_name):
        raise OFSException('Invalid bucket: %s' % bucket_name)
    return self._get_bucket(bucket_name)