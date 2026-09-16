def check_repository_url(self):
    repository_url = self.repository_config['repository']
    if repository_url.startswith((repository.LEGACY_PYPI, repository.
        LEGACY_TEST_PYPI)):
        raise exceptions.UploadToDeprecatedPyPIDetected.from_args(
            repository_url, utils.DEFAULT_REPOSITORY, utils.TEST_REPOSITORY)