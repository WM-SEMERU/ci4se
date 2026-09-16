def get_changes(self, remove=True, only_current=False, resources=None,
    task_handle=taskhandle.NullTaskHandle()):
    changes = ChangeSet('Inline method <%s>' % self.name)
    if resources is None:
        resources = self.project.get_python_files()
    if only_current:
        resources = [self.original]
        if remove:
            resources.append(self.resource)
    job_set = task_handle.create_jobset('Collecting Changes', len(resources))
    for file in resources:
        job_set.started_job(file.path)
        if file == self.resource:
            changes.add_change(self._defining_file_changes(changes, remove=
                remove, only_current=only_current))
        else:
            aim = None
            if only_current and self.original == file:
                aim = self.offset
            handle = _InlineFunctionCallsForModuleHandle(self.project, file,
                self.others_generator, aim)
            result = move.ModuleSkipRenamer(self.occurrence_finder, file,
                handle).get_changed_module()
            if result is not None:
                result = _add_imports(self.project, result, file, self.imports)
                if remove:
                    result = _remove_from(self.project, self.pyname, result,
                        file)
                changes.add_change(ChangeContents(file, result))
        job_set.finished_job()
    return changes