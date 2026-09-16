def list_security_groups(self, retrieve_all=True, **_params):
    return self.list('security_groups', self.security_groups_path,
        retrieve_all, **_params)