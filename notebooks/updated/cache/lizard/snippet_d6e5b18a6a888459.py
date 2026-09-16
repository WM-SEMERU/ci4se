def search_normalize(self, results):
    for sshkey in results:
        sshkey['user_id'] = self.user.id
    return super(SSHKey, self).search_normalize(results)