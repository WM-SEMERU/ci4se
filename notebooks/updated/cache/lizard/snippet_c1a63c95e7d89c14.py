def delete_hook(self, auth, username, repo_name, hook_id):
    path = '/repos/{u}/{r}/hooks/{i}'.format(u=username, r=repo_name, i=hook_id
        )
    self.delete(path, auth=auth)