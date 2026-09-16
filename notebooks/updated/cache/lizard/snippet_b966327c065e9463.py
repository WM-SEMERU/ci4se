def throw_to(self, target, *a):
    self.ready.append((getcurrent(), ()))
    return target.throw(*a)