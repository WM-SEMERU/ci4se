def update(self, message=None, subject=None, days=None, downloads=None,
    notify=None):
    method, url = get_URL('update')
    payload = {'apikey': self.config.get('apikey'), 'logintoken': self.
        session.cookies.get('logintoken'), 'transferid': self.transfer_id}
    data = {'message': message or self.transfer_info.get('message'),
        'message': subject or self.transfer_info.get('subject'), 'days': 
        days or self.transfer_info.get('days'), 'downloads': downloads or
        self.transfer_info.get('downloads'), 'notify': notify or self.
        transfer_info.get('notify')}
    payload.update(data)
    res = getattr(self.session, method)(url, params=payload)
    if res.status_code:
        self.transfer_info.update(data)
        return True
    hellraiser(res)