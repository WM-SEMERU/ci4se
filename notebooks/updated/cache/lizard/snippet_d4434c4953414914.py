def as_issue(self):
    headers, data = self._requester.requestJsonAndCheck('GET', self.issue_url)
    return github.Issue.Issue(self._requester, headers, data, completed=True)