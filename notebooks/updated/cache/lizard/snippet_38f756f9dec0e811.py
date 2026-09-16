def push_current(self, project):
    if __debug__:
        from .targets import ProjectTarget
        assert isinstance(project, ProjectTarget)
    self.saved_current_project.append(self.current_project)
    self.current_project = project