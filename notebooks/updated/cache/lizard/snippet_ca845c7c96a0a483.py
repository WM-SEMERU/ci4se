def friendConnect(self, friend_id):
    data = {'to_friend': friend_id, 'action': 'confirm'}
    r = self._post(self.req_url.CONNECT, data)
    return r.ok