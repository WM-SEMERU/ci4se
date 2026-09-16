def spawn(self, process):
    self._assert_started()
    process.bind(self)
    self.http.mount_process(process)
    self._processes[process.pid] = process
    process.initialize()
    return process.pid