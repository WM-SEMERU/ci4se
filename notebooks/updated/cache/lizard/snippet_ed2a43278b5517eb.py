def sync_results_to_new_location(self, worker_ip):
    if worker_ip != self._log_syncer.worker_ip:
        self._log_syncer.set_worker_ip(worker_ip)
        self._log_syncer.sync_to_worker_if_possible()