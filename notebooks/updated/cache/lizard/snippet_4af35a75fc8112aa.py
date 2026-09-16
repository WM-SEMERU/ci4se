def mark_read(self):
    raise NotImplementedError(
        'The Kippt API does not yet support marking notifications as read.')
    data = json.dumps({'action': 'mark_seen'})
    r = requests.post('https://kippt.com/api/notifications', headers=self.
        kippt.header, data=data)
    return r.json()