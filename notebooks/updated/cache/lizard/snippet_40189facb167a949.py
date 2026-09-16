def _WorkerCommand_executable(self):
    worker = self.workersArguments
    c = []
    if worker.executable:
        c.append(worker.executable)
    if worker.args:
        if self.isLocal():
            c.extend(['{0}'.format(a) for a in worker.args])
        else:
            c.extend(['"{0}"'.format(a.replace('"', '\\"')) for a in worker
                .args])
    return c