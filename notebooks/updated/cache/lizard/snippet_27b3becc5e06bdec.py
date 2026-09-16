def symlink(self, req, link, parent, name):
    self.reply_err(req, errno.EROFS)