def set_project_id(self, project_id):
    self._project_id = project_id
    if self == Context._global_context:
        try:
            from google.datalab import Context as new_context
            new_context.default().set_project_id(project_id)
        except ImportError:
            pass