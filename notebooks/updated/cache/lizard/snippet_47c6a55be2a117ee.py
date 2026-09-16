def _project_auto_open(self):
    for project in self._projects.values():
        if project.auto_open:
            yield from project.open()