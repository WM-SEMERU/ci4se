def worklogs(self, issue):
    r_json = self._get_json('issue/' + str(issue) + '/worklog')
    worklogs = [Worklog(self._options, self._session, raw_worklog_json) for
        raw_worklog_json in r_json['worklogs']]
    return worklogs