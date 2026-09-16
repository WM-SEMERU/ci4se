def create_issue_link(self, type, inwardIssue, outwardIssue, comment=None):
    if not hasattr(self, '_cached_issuetypes'):
        self._cached_issue_link_types = self.issue_link_types()
    if type not in self._cached_issue_link_types:
        for lt in self._cached_issue_link_types:
            if lt.outward == type:
                type = lt.name
                break
            elif lt.inward == type:
                type = lt.name
                inwardIssue, outwardIssue = outwardIssue, inwardIssue
                break
    data = {'type': {'name': type}, 'inwardIssue': {'key': inwardIssue},
        'outwardIssue': {'key': outwardIssue}, 'comment': comment}
    url = self._get_url('issueLink')
    return self._session.post(url, data=json.dumps(data))