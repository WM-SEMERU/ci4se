def inspect_workers(self):
    workers = tuple(self.workers.values())
    expired = tuple(w for w in workers if not w.is_alive())
    for worker in expired:
        self.workers.pop(worker.pid)
    return ((w.pid, w.exitcode) for w in expired if w.exitcode != 0)