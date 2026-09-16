def _Members(self, group):
    group.members = set(group.members).union(self.gids.get(group.gid, []))
    return group