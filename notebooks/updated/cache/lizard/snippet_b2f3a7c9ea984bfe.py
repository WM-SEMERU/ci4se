def sort(self):
    self.sorted = list()
    self.pushed = set()
    for item in self.unsorted:
        popped = []
        self.push(item)
        while len(self.stack):
            try:
                top = self.top()
                ref = next(top[1])
                refd = self.index.get(ref)
                if refd is None:
                    log.debug('"%s" not found, skipped', Repr(ref))
                    continue
                self.push(refd)
            except StopIteration:
                popped.append(self.pop())
                continue
        for p in popped:
            self.sorted.append(p)
    self.unsorted = self.sorted
    return self.sorted