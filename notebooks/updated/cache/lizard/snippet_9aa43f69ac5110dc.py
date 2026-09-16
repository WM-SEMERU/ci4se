def add_project(self):
    i = self.prj_tablev.currentIndex()
    item = i.internalPointer()
    if item:
        project = item.internal_data()
        if self._atype:
            self._atype.projects.add(project)
        elif self._dep:
            self._dep.projects.add(project)
        else:
            project.users.add(self._user)
        self.projects.append(project)
        item.set_parent(None)