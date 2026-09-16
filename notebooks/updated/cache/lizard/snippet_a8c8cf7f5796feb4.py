def cached(self, dependency):
    if dependency.threadlocal:
        return getattr(self._local, dependency.name, None)
    elif dependency.singleton:
        return self._singleton.get(dependency.name)