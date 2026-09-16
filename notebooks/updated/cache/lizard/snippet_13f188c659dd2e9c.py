def chown(self, path, user='', group=''):
    _complain_ifclosed(self.closed)
    return self.fs.chown(path, user, group)