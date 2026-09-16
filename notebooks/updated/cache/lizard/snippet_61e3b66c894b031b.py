def create_project(self, name, **kwargs):
    data = self._wrap_dict('project', kwargs)
    data['customer']['name'] = name
    return self.post('/projects.json', data=data)