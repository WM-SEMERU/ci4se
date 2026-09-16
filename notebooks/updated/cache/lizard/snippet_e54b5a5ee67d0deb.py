def heartbeat(self):
    mode = self.task_master.get_mode()
    self.task_master.worker_heartbeat(self.worker_id, mode, self.lifetime,
        self.environment(), parent=self.parent)
    return mode