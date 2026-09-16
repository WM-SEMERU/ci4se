def prioritize(self, item, force=False):
    with self.condition:
        if item in self.working or item in self.force:
            return
        self.queue.remove(item)
        if force:
            self.force.append(item)
        else:
            self.queue.appendleft(item)
        self.condition.notify_all()