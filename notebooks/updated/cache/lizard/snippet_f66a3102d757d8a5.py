def source_add_update(self, crits_id, crits_type, source, action_type='add',
    method='', reference='', date=None):
    type_trans = self._type_translation(crits_type)
    submit_url = '{}/{}/{}/'.format(self.url, type_trans, crits_id)
    if date is None:
        date = datetime.datetime.now()
        date = datetime.datetime.strftime(date, '%Y-%m-%d %H:%M:%S.%f')
    params = {'api_key': self.api_key, 'username': self.username}
    data = {'action': 'source_add_update', 'action_type': action_type,
        'source': source, 'method': method, 'reference': reference, 'date':
        date}
    r = requests.patch(submit_url, params=params, data=json.dumps(data),
        proxies=self.proxies, verify=self.verify)
    if r.status_code == 200:
        log.debug('Source {0} added successfully to {1} {2}'.format(source,
            crits_type, crits_id))
        return True
    else:
        log.error(
            'Error with status code {0} and message {1} for type {2} and id {3} and source {4}'
            .format(r.status_code, r.text, crits_type, crits_id, source))
        return False