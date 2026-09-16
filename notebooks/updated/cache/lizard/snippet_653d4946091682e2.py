def update_hook(self, auth, repo_name, hook_id, update, organization=None):
    if organization is not None:
        path = '/repos/{o}/{r}/hooks/{i}'.format(o=organization, r=
            repo_name, i=hook_id)
    else:
        path = '/repos/{r}/hooks/{i}'.format(r=repo_name, i=hook_id)
    response = self._patch(path, auth=auth, data=update.as_dict())
    return GogsRepo.Hook.from_json(response.json())