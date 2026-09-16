def get_branches(self, auth, username, repo_name):
    path = '/repos/{u}/{r}/branches'.format(u=username, r=repo_name)
    response = self.get(path, auth=auth)
    return [GogsBranch.from_json(branch_json) for branch_json in response.
        json()]