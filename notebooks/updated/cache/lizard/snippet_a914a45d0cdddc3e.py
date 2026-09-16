def add(self, target, *args, **kwargs):
    t = Thread.run(target.__name__, target, *args, **kwargs)
    self.threads.append(t)