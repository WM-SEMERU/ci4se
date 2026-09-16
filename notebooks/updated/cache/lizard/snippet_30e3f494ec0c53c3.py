def has_auth_params(self, scheme):
    for k, v in iteritems(self.schemes[scheme]['params']):
        if not v:
            return False
    return True