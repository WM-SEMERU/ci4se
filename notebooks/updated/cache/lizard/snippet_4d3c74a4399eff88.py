def get_project_filenames(self):
    recent_files = []
    if self.current_active_project:
        recent_files = self.current_active_project.get_recent_files()
    elif self.latest_project:
        recent_files = self.latest_project.get_recent_files()
    return recent_files