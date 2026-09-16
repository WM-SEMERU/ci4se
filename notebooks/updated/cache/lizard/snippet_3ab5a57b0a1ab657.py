def addPolicyURI(self, policy_uri):
    if policy_uri == AUTH_NONE:
        raise RuntimeError(
            'To send no policies, do not set any on the response.')
    if policy_uri not in self.auth_policies:
        self.auth_policies.append(policy_uri)