def delete(self):
    fcid = None
    pid = None
    if isinstance(self, File):
        fcid = self.fid
        pid = self.cid
    elif isinstance(self, Directory):
        fcid = self.cid
        pid = self.pid
    else:
        raise APIError('Invalid BaseFile instance.')
    if not self._deleted:
        if self.api._req_rb_delete(fcid, pid):
            self._deleted = True
            return True
    else:
        raise APIError('This file or directory is already deleted.')