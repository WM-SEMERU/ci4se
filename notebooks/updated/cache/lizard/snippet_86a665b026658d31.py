def set_backend(self, backend):
    self.backend = backend
    self.dagobah_id = self.backend.get_new_dagobah_id()
    for job in self.jobs:
        job.backend = backend
        for task in job.tasks.values():
            task.backend = backend
    self.commit(cascade=True)