def mkdir(self, req, parent, name, mode):
    self.reply_err(req, errno.EROFS)