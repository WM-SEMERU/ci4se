def membership_in(self, organization):
    url = self._build_url('user', 'memberships', 'orgs', str(organization))
    json = self._json(self._get(url), 200)
    return Membership(json, self)