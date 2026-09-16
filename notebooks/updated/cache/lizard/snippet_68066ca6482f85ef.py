def removed_issues(self, board_id, sprint_id):
    r_json = self._get_json(
        'rapid/charts/sprintreport?rapidViewId=%s&sprintId=%s' % (board_id,
        sprint_id), base=self.AGILE_BASE_URL)
    issues = [Issue(self._options, self._session, raw_issues_json) for
        raw_issues_json in r_json['contents']['puntedIssues']]
    return issues