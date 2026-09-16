def notify_watches(self, oldval, newval):
    watches = self._watches.copy()
    for k in watches:
        fn = watches[k]
        if isinstance(fn, collections.Callable):
            fn(k, self, oldval, newval)