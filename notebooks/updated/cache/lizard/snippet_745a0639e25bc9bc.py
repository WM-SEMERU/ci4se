def pull_request(self, owner, repository, number):
    r = self.repository(owner, repository)
    return r.pull_request(number) if r else None