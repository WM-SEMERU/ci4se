def timeout(self, duration=3600):
    self.room.check_owner()
    self.conn.make_call('timeoutFile', self.fid, duration)