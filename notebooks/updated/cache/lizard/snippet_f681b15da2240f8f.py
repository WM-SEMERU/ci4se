def notify(self, n=1):
    if not is_locked(self._lock):
        raise RuntimeError('lock is not locked')
    notified = [0]

    def walker(switcher, predicate):
        if not switcher.active:
            return False
        if predicate and not predicate():
            return True
        if n >= 0 and notified[0] >= n:
            return True
        switcher.switch()
        notified[0] += 1
        return False
    walk_callbacks(self, walker)