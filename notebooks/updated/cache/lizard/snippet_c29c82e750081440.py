def HeadList(self):
    return [(rname, repo.currenthead) for rname, repo in self.repos.items()]