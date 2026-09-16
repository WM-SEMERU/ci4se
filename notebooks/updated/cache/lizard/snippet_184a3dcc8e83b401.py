def create_request_comment(self, issue_id_or_key, body, public=True):
    log.warning('Creating comment...')
    data = {'body': body, 'public': public}
    return self.post('rest/servicedeskapi/request/{}/comment'.format(
        issue_id_or_key), data=data)