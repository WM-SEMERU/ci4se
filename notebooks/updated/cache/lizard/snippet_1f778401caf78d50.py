def map_sid2sub(self, sid, sub):
    self.set('sid2sub', sid, sub)
    self.set('sub2sid', sub, sid)