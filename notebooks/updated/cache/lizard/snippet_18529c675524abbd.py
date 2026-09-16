def create_head(self, path, commit='HEAD', force=False, logmsg=None):
    return Head.create(self, path, commit, force, logmsg)