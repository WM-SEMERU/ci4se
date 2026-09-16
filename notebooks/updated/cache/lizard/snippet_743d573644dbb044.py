def chown(self, uid, gid):
    self.sftp._log(DEBUG, 'chown(%s, %r, %r)' % (hexlify(self.handle), uid,
        gid))
    attr = SFTPAttributes()
    attr.st_uid, attr.st_gid = uid, gid
    self.sftp._request(CMD_FSETSTAT, self.handle, attr)