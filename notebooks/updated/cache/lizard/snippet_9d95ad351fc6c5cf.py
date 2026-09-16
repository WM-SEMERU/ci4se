def get_pythonpath(self, at_start=False):
    if at_start:
        current_path = self.get_option('current_project_path', default=None)
    else:
        current_path = self.get_active_project_path()
    if current_path is None:
        return []
    else:
        return [current_path]