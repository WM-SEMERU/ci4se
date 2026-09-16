def create_github_client(self, project):
    token = self._get_installation_key(project=project)
    if not token:
        LOGGER.warning(
            "Could not find an authentication token for '%s'. Do you have access to this repository?"
            , project)
        return
    gh = github3.GitHubEnterprise(self.base_url)
    gh.login(token=token)
    return gh