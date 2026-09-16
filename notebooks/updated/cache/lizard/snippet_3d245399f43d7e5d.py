def _get_repos(self):
    result = {}
    for xmlpath in self.installed:
        repo = RepositorySettings(self, xmlpath)
        result[repo.name.lower()] = repo
    return result