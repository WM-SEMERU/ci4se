def package_repositories(self):
    if self._package_repository_manager is None:
        self._package_repository_manager = PackageRepositoryManager(session
            =self._session)
    return self._package_repository_manager