def create_issues_report(self, timeout=-1):
    uri = '{}/issues/'.format(self.data['uri'])
    return self._helper.create_report(uri, timeout)