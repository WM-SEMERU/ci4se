def get_lock_requests(self):
    d = defaultdict(list)
    if self._context:
        for variant in self._context.resolved_packages:
            name = variant.name
            version = variant.version
            lock = self.patch_locks.get(name)
            if lock is None:
                lock = self.default_patch_lock
            request = get_lock_request(name, version, lock)
            if request is not None:
                d[lock].append(request)
    return d