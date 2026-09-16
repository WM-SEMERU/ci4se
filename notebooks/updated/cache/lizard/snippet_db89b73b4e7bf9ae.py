def ignore(self, matcher):
    events = self.eventtree.findAndRemove(matcher)
    for e in events:
        self.queue.unblock(e)
        e.canignore = True