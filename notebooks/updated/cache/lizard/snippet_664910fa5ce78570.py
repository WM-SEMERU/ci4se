def command_repo_info(self):
    if len(self.args) == 2 and self.args[0] == 'repo-info' and self.args[1
        ] in RepoList().all_repos:
        del RepoList().all_repos
        RepoInfo().view(self.args[1])
    elif len(self.args) > 1 and self.args[0] == 'repo-info' and self.args[1
        ] not in RepoList().all_repos:
        usage(self.args[1])
    else:
        usage('')