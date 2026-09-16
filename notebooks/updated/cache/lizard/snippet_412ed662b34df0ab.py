def branch(self):
    result = get_branch(repo=self.repo)
    if result is None:
        result = get_travis_branch()
    return result