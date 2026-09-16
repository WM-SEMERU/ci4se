def map_sid2uid(self, sid, uid):
    self.set('sid2uid', sid, uid)
    self.set('uid2sid', uid, sid)