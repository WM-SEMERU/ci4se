def get_acl(self, validate=True, headers=None, version_id=None):
    if not self.bucket_name:
        raise InvalidUriError('get_acl on bucket-less URI (%s)' % self.uri)
    bucket = self.get_bucket(validate, headers)
    acl = bucket.get_acl(self.object_name, headers, version_id)
    self.check_response(acl, 'acl', self.uri)
    return acl