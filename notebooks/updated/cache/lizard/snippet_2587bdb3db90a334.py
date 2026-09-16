def InferUserAndSubjectFromUrn(self):
    _, hunts_str, hunt_id, user, _ = self.urn.Split(5)
    if hunts_str != 'hunts':
        raise access_control.UnauthorizedAccess(
            'Approval object has invalid urn %s.' % self.urn,
            requested_access=self.token.requested_access)
    return user, aff4.ROOT_URN.Add('hunts').Add(hunt_id)