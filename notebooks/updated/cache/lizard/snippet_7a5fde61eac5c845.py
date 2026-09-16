def get_project(self, project_id):
    return youtrack.Project(self._get('/admin/project/' + urlquote(
        project_id)), self)