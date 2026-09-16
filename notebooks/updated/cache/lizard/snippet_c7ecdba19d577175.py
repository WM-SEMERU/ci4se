def copy(self):
    other = ContextModel(self._context, self.parent())
    other._stale = self._stale
    other._modified = self._modified
    other.request = self.request[:]
    other.packages_path = self.packages_path
    other.implicit_packages = self.implicit_packages
    other.package_filter = self.package_filter
    other.caching = self.caching
    other.default_patch_lock = self.default_patch_lock
    other.patch_locks = copy.deepcopy(self.patch_locks)
    return other