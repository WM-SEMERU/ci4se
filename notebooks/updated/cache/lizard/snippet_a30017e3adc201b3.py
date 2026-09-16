def grant(self, lock, unit):
    if not hookenv.is_leader():
        return False
    granted = set()
    for u in self.grants:
        if lock in self.grants[u]:
            granted.add(u)
    if unit in granted:
        return True
    reqs = set()
    for u in self.requests:
        if u in granted:
            continue
        for _lock, ts in self.requests[u].items():
            if _lock == lock:
                reqs.add((ts, u))
    queue = [t[1] for t in sorted(reqs)]
    if unit not in queue:
        return False
    grant_func = getattr(self, 'grant_{}'.format(lock), self.default_grant)
    if grant_func(lock, unit, granted, queue):
        self.msg('Leader grants {} to {}'.format(lock, unit))
        self.grants.setdefault(unit, {})[lock] = self.requests[unit][lock]
        return True
    return False