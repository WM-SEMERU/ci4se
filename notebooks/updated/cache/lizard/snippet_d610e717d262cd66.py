def get_milestone(self, title):
    if not title:
        return GithubObject.NotSet
    if not hasattr(self, '_milestones'):
        self._milestones = {m.title: m for m in self.repo.get_milestones()}
    milestone = self._milestones.get(title)
    if not milestone:
        milestone = self.repo.create_milestone(title=title)
    return milestone