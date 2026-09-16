def members(self):
    allmembers = set()
    for team in self.teams():
        allmembers.update(team.members())
    return sorted(allmembers)