def repo_tools(self, repo, branch, version):
    try:
        tools = []
        status = self.path_dirs.apply_path(repo)
        if status[0]:
            cwd = status[1]
        else:
            self.logger.error(
                'apply_path failed. Exiting repo_tools with status: ' + str
                (status))
            return status
        status = True, None
        if status[0]:
            path, _, _ = self.path_dirs.get_path(repo)
            tools = AvailableTools(path, version=version)
        else:
            self.logger.error(
                'checkout failed. Exiting repo_tools with status: ' + str(
                status))
            return status
        chdir(cwd)
        status = True, tools
    except Exception as e:
        self.logger.error('repo_tools failed with error: ' + str(e))
        status = False, e
    return status