def get_acl(self, key_name='', headers=None, version_id=None):
    return self.get_acl_helper(key_name, headers, STANDARD_ACL)