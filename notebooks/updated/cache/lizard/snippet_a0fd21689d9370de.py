def get_newest_commit_date(self):
    newest_commit = self.get_newest_commit()
    return self.git.get_commit_date(newest_commit, self.tz_name)