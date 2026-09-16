def update(self, case_id, **attributes):
    response = self._thehive.do_patch('/api/case/{}'.format(case_id), **
        attributes)
    if response.status_code == requests.codes.unauthorized:
        raise TheHiveException('Authentication failed')
    if self.status_ok(response.status_code):
        return self(response.json()['id'])
    else:
        raise CaseException('Server returned {}: {}'.format(response.
            status_code, response.text))