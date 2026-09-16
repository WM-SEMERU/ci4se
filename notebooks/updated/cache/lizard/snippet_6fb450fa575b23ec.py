def destroy(self, force=False):
    try:
        if not force:
            self.join()
    finally:
        self._dbg(2, 'Destroying queue...')
        self.workqueue.destroy()
        self.account_manager.reset()
        self.completed = 0
        self.total = 0
        self.failed = 0
        self.status_bar_length = 0
        self._dbg(2, 'Queue destroyed.')
        self._del_status_bar()