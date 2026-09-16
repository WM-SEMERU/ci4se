def create(self, model_name):
    body = {'name': model_name}
    parent = 'projects/' + self._project_id
    return self._api.projects().models().create(body=body, parent=parent
        ).execute()