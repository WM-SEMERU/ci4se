def _auto_commit(self):
    if not self.auto_commit or self.auto_commit_every_n is None:
        return
    if self.count_since_commit >= self.auto_commit_every_n:
        self.commit()