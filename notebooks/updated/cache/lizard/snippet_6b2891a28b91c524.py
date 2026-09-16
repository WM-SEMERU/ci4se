def chmod(self, mode):
    self.sftp._log(DEBUG, 'chmod(%s, %r)' % (hexlify(self.handle), mode))
    attr = SFTPAttributes()
    attr.st_mode = mode
    self.sftp._request(CMD_FSETSTAT, self.handle, attr)