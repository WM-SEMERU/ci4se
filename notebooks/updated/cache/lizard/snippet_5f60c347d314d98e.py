def get_project(self, project_id):
    try:
        UUID(project_id, version=4)
    except ValueError:
        raise aiohttp.web.HTTPBadRequest(text=
            'Project ID {} is not a valid UUID'.format(project_id))
    if project_id not in self._projects:
        raise aiohttp.web.HTTPNotFound(text="Project ID {} doesn't exist".
            format(project_id))
    return self._projects[project_id]