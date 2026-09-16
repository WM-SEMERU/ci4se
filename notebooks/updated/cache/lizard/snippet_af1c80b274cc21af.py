def get_deploy_key(self, auth, username, repo_name, key_id):
    response = self.get('/repos/{u}/{r}/keys/{k}'.format(u=username, r=
        repo_name, k=key_id), auth=auth)
    return GogsRepo.DeployKey.from_json(response.json())