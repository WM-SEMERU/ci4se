def install(self, xmlpath):
    from os import path
    fullpath = path.abspath(path.expanduser(xmlpath))
    if path.isfile(fullpath):
        repo = RepositorySettings(self, fullpath)
        if repo.name.lower() not in self.repositories:
            self.installed.append(fullpath)
            self._save_installed()
            self.archive[repo.name.lower()] = {}
            self._save_archive()
            self.repositories[repo.name.lower()] = repo
    else:
        warn('The file {} does not exist; install aborted.'.format(fullpath))