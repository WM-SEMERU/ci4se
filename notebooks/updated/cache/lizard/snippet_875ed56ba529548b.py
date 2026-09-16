def workers(self, alive=True):
    return self.registry.filter(WORKER_OBSERVED_MODE, priority_min=alive and
        time.time() or '-inf')