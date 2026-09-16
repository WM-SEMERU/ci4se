def InferUserAndSubjectFromUrn(self):
    _, cron_str, cron_job_name, user, _ = self.urn.Split(5)
    if cron_str != 'cron':
        raise access_control.UnauthorizedAccess(
            'Approval object has invalid urn %s.' % self.urn,
            requested_access=self.token.requested_access)
    return user, aff4.ROOT_URN.Add('cron').Add(cron_job_name)