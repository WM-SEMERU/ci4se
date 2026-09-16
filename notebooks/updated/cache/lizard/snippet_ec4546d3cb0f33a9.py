def AddGroupMemberships(self):
    self.groups = {g.name: self._Members(g) for g in itervalues(self.groups)}
    for g in itervalues(self.groups):
        for user in g.members:
            membership = self.memberships.setdefault(user, set())
            membership.add(g.gid)
    for user in itervalues(self.entry):
        user.gids = self.memberships.get(user.username)