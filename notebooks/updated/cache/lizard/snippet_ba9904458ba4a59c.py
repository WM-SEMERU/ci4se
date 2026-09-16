def unblockall(self):
    for q in self.queues.values():
        q.unblockall()
    self.blockEvents.clear()