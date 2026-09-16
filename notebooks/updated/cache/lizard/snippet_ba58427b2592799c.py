def get_supported_permissions(self):
    if not hasattr(self, '_perms_cache'):
        if self.includes and isinstance(self.includes, collections.Callable):
            includes = self.includes(self)
        else:
            includes = self.includes or []
        if self.excludes and isinstance(self.excludes, collections.Callable):
            excludes = self.excludes(self)
        else:
            excludes = self.excludes or []
        includes = set(includes)
        excludes = set(excludes)
        includes = includes.difference(excludes)
        self._perms_cache = includes
    return self._perms_cache