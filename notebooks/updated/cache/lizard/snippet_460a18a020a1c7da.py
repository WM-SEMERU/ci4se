def add_device(self, model, serial):
    device = {'model': model, 'vendor': self.vendor(), 'sn': serial, 'type':
        'vendor'}
    headers = {'User-Agent': self.user_agent()}
    headers.update(self.headers())
    r = requests.post(self.portals_url() + '/portals/' + self.portal_id() +
        '/devices', data=json.dumps(device), headers=headers, auth=self.auth())
    if HTTP_STATUS.ADDED == r.status_code:
        device_obj = r.json()
        return dictify_device_meta(device_obj)
    else:
        print('add_device: Something went wrong: <{0}>: {1}'.format(r.
            status_code, r.reason))
        r.raise_for_status()