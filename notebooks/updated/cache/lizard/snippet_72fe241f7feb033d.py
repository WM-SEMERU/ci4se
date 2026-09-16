def count(self, paths='', **kwargs):
    if paths:
        return len(self.repo.git.rev_list(self.hexsha, '--', paths, **
            kwargs).splitlines())
    else:
        return len(self.repo.git.rev_list(self.hexsha, **kwargs).splitlines())