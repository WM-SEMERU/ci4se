def generate_modules_cache(self, modules, underlined=None, task_handle=
    taskhandle.NullTaskHandle()):
    job_set = task_handle.create_jobset(
        'Generatig autoimport cache for modules', len(modules))
    for modname in modules:
        job_set.started_job('Working on <%s>' % modname)
        if modname.endswith('.*'):
            mod = self.project.find_module(modname[:-2])
            if mod:
                for sub in submodules(mod):
                    self.update_resource(sub, underlined)
        else:
            self.update_module(modname, underlined)
        job_set.finished_job()