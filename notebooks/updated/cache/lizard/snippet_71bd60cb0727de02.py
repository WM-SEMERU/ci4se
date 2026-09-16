def _reschedule(self, node):
    if node.shutting_down:
        return
    if not self.workqueue:
        node.shutdown()
        return
    self.log('Number of units waiting for node:', len(self.workqueue))
    if self._pending_of(self.assigned_work[node]) > 2:
        return
    self._assign_work_unit(node)