def get_diff(self, commit, other_commit):
    print(other_commit, 'VS', commit)
    diff = self.repo.git.diff(commit, other_commit)
    return Diff(diff).get_totals()